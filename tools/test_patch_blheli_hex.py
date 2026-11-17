#!/usr/bin/env python3
"""Independent checks for tools/patch_blheli_hex.py.

Runs the patcher as a separate process and checks its output with its own
parser, so the script is not grading itself.

Usage:
    STOCK_HEX=path/to/A_H_25_REV16_7.HEX \
    ORIGINAL_ESC1=path/to/A_H_25_REV16_7_ESC1_BIDIR.HEX \
    ORIGINAL_ESC2=path/to/A_H_25_REV16_7_ESC2_BIDIR_REV.HEX \
    python -m unittest -v tools/test_patch_blheli_hex.py

STOCK_HEX is required. ORIGINAL_ESC1 and ORIGINAL_ESC2 are the files that were
actually flashed; the byte-for-byte test is skipped if they are not given.
"""

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("patch_blheli_hex.py")
STOCK = os.environ.get("STOCK_HEX")

# The Session 006 patch table, written out again here on purpose.
TABLE = {0x1A09: 0x08, 0x1A19: 0x00, 0x1A1A: 0xFF, 0x1A21: 0x7D}
DIRECTION = {
    "A_H_25_REV16_7_ESC1_BIDIR.HEX": 0x03,
    "A_H_25_REV16_7_ESC2_BIDIR_REV.HEX": 0x04,
}
ORIGINALS = {
    "A_H_25_REV16_7_ESC1_BIDIR.HEX": os.environ.get("ORIGINAL_ESC1"),
    "A_H_25_REV16_7_ESC2_BIDIR_REV.HEX": os.environ.get("ORIGINAL_ESC2"),
}


def records(path):
    """Yield (line number, raw bytes) for each record."""
    for n, line in enumerate(Path(path).read_text().splitlines(), 1):
        yield n, bytes.fromhex(line[1:])


def data_bytes(path):
    """Map absolute address -> byte for every data record."""
    mem, base = {}, 0
    for _, raw in records(path):
        count, offset, rtype = raw[0], int.from_bytes(raw[1:3], "big"), raw[3]
        if rtype == 0x04:
            base = int.from_bytes(raw[4:6], "big") << 16
        elif rtype == 0x00:
            for k in range(count):
                mem[base + offset + k] = raw[4 + k]
    return mem


def run(stock, out_dir):
    return subprocess.run([sys.executable, str(SCRIPT), str(stock), "-o", str(out_dir)],
                          capture_output=True, text=True)


@unittest.skipUnless(STOCK, "set STOCK_HEX to the stock A_H_25_REV16_7.HEX")
class PatchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.out = Path(cls.tmp.name)
        result = run(STOCK, cls.out)
        if result.returncode != 0:
            raise AssertionError(f"patcher failed: {result.stderr}")
        print("\n" + result.stdout.strip())
        cls.stock = data_bytes(STOCK)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_patched_bytes_match_table_and_nothing_else_changed(self):
        for name, direction in DIRECTION.items():
            with self.subTest(file=name):
                expected = {**TABLE, 0x1A0B: direction}
                out = data_bytes(self.out / name)
                self.assertEqual(set(out), set(self.stock), "address set differs")
                changed = {a: v for a, v in out.items() if v != self.stock[a]}
                self.assertEqual(changed, expected)
                print(f"\n  {name}: {len(out)} data bytes, changed only "
                      + ", ".join(f"{a:#06x}={v:#04x}" for a, v in sorted(changed.items())))

    def test_every_record_checksum_is_valid(self):
        for name in DIRECTION:
            with self.subTest(file=name):
                recs = list(records(self.out / name))
                bad = [n for n, raw in recs if sum(raw) & 0xFF]
                self.assertEqual(bad, [])
                print(f"\n  {name}: {len(recs)} records, all checksums valid")

    def test_matches_originally_flashed_files_byte_for_byte(self):
        if not all(ORIGINALS.values()):
            self.skipTest("set ORIGINAL_ESC1 and ORIGINAL_ESC2")
        for name, original in ORIGINALS.items():
            with self.subTest(file=name):
                ours = (self.out / name).read_bytes()
                theirs = Path(original).read_bytes()
                self.assertEqual(ours, theirs)
                print(f"\n  {name}: identical to {Path(original).name} ({len(ours)} bytes)")

    def test_rejects_bad_checksum_in_input(self):
        lines = Path(STOCK).read_text().splitlines(keepends=True)
        lines[100] = lines[100][:-3] + ("00" if lines[100][-3:-1] != "00" else "01") + "\n"
        self._expect_rejection(lines, "bad checksum")

    def test_rejects_file_that_is_not_the_expected_stock(self):
        lines = Path(STOCK).read_text().splitlines(keepends=True)
        idx = next(i for i, l in enumerate(lines) if l.startswith(":0D1A1D00"))
        raw = bytearray.fromhex(lines[idx][1:].strip())
        raw[8] = 0x7D                      # Center_Throttle already patched
        raw[-1] = (-sum(raw[:-1])) & 0xFF  # keep the checksum valid
        lines[idx] = ":" + raw.hex().upper() + "\n"
        self._expect_rejection(lines, "not the expected stock file")

    def _expect_rejection(self, lines, message):
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "bad.HEX"
            bad.write_text("".join(lines))
            result = run(bad, Path(tmp) / "out")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn(message, result.stderr)
            self.assertFalse((Path(tmp) / "out").exists(), "wrote output despite bad input")
            print(f"\n  rejected as expected: {result.stderr.strip()}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
