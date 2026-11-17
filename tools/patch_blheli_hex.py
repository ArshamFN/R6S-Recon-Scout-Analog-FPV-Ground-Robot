#!/usr/bin/env python3
"""Rebuild the Session 006 patched BLHeli_S hex files from the stock firmware.

Reads the stock A_H_25_REV16_7.HEX (BLHeli_S 16.7, from bitdump/BLHeli), applies
the EEPROM byte changes from the Session 006 patch table, recalculates the
checksum of every record it changes, validates every record in the output, and
writes one file per ESC.

Usage:
    python tools/patch_blheli_hex.py path/to/A_H_25_REV16_7.HEX [-o OUTPUT_DIR]

OUTPUT_DIR defaults to the folder that holds the stock file.
"""

import argparse
import sys
from pathlib import Path

# Session 006 patch table: address -> (name, stock value, patched value).
COMMON_PATCH = {
    0x1A09: ("Startup_Pwr", 0x09, 0x08),
    0x1A19: ("Min_Throttle", 0x25, 0x00),
    0x1A1A: ("Max_Throttle", 0xD0, 0xFF),
    0x1A21: ("Center_Throttle", 0x7A, 0x7D),
}
DIRECTION_ADDR = 0x1A0B
DIRECTION_STOCK = 0x01

# Output file name -> Direction byte (3 = Bidirectional, 4 = Bidirectional Reversed).
OUTPUTS = {
    "A_H_25_REV16_7_ESC1_BIDIR.HEX": 0x03,
    "A_H_25_REV16_7_ESC2_BIDIR_REV.HEX": 0x04,
}

# Bytes that identify the expected stock file. From the EEPROM segment in
# BLHeli_S.asm: firmware 16.7, EEPROM layout revision 33, layout tag #A_H_25#.
IDENTITY = {0x1A00: 16, 0x1A01: 7, 0x1A02: 33}
LAYOUT_TAG_ADDR = 0x1A40
LAYOUT_TAG = b"#A_H_25#"


class HexError(Exception):
    """Raised when a file is not valid Intel HEX or is not the expected stock file."""


def split_eol(line):
    """Split a line into its text and its line ending, so endings are preserved."""
    text = line.rstrip("\r\n")
    return text, line[len(text):]


def parse_record(text, line_no):
    """Decode one record and check its length and checksum. Returns the raw bytes."""
    if not text.startswith(":"):
        raise HexError(f"line {line_no}: missing ':' start code")
    try:
        raw = bytes.fromhex(text[1:])
    except ValueError:
        raise HexError(f"line {line_no}: not valid hex") from None
    if len(raw) < 5 or len(raw) != raw[0] + 5:
        raise HexError(f"line {line_no}: length does not match byte count")
    if sum(raw) & 0xFF:
        raise HexError(f"line {line_no}: bad checksum")
    return raw


def memory_map(lines):
    """Validate every record and map each data byte's absolute address to
    (value, line index, position in the record's data)."""
    mem = {}
    base = 0
    seen_eof = False
    for i, line in enumerate(lines):
        text, _ = split_eol(line)
        if seen_eof:
            raise HexError(f"line {i + 1}: content after end-of-file record")
        raw = parse_record(text, i + 1)
        count, offset, rtype = raw[0], (raw[1] << 8) | raw[2], raw[3]
        data = raw[4:4 + count]
        if rtype == 0x00:
            for pos, value in enumerate(data):
                addr = base + offset + pos
                if addr in mem:
                    raise HexError(f"line {i + 1}: address {addr:#06x} defined twice")
                mem[addr] = (value, i, pos)
        elif rtype == 0x01:
            seen_eof = True
        elif rtype == 0x02:
            base = ((data[0] << 8) | data[1]) << 4
        elif rtype == 0x04:
            base = ((data[0] << 8) | data[1]) << 16
        elif rtype not in (0x03, 0x05):
            raise HexError(f"line {i + 1}: unknown record type {rtype:#04x}")
    if not seen_eof:
        raise HexError("no end-of-file record")
    return mem


def check_stock(mem):
    """Refuse to patch anything other than the expected stock file."""
    expected = dict(IDENTITY)
    expected.update({LAYOUT_TAG_ADDR + k: b for k, b in enumerate(LAYOUT_TAG)})
    expected.update({addr: stock for addr, (_, stock, _) in COMMON_PATCH.items()})
    expected[DIRECTION_ADDR] = DIRECTION_STOCK
    for addr, value in expected.items():
        if addr not in mem:
            raise HexError(f"not the expected stock file: address {addr:#06x} is missing")
        if mem[addr][0] != value:
            raise HexError(
                f"not the expected stock file: {addr:#06x} is {mem[addr][0]:#04x}, "
                f"expected {value:#04x}"
            )


def apply_patch(lines, mem, changes):
    """Return new lines with the changes applied and each changed record's
    checksum recalculated. Unchanged records are copied as they are."""
    edits = {}
    for addr, value in changes.items():
        _, idx, pos = mem[addr]
        edits.setdefault(idx, {})[pos] = value
    out = list(lines)
    for idx, by_pos in edits.items():
        text, eol = split_eol(lines[idx])
        raw = bytearray(bytes.fromhex(text[1:]))
        for pos, value in by_pos.items():
            raw[4 + pos] = value
        raw[-1] = (-sum(raw[:-1])) & 0xFF
        out[idx] = ":" + raw.hex().upper() + eol
    return out, sorted(edits)


def verify_output(stock_mem, out_lines, changes, changed_lines, stock_lines):
    """Check the patched file: every record valid, patched bytes hold the new
    values, every other byte and every unchanged record is identical to stock."""
    out_mem = memory_map(out_lines)
    if set(out_mem) != set(stock_mem):
        raise HexError("output covers different addresses than the stock file")
    for addr, (value, _, _) in out_mem.items():
        expected = changes.get(addr, stock_mem[addr][0])
        if value != expected:
            raise HexError(f"output {addr:#06x} is {value:#04x}, expected {expected:#04x}")
    for i, (a, b) in enumerate(zip(stock_lines, out_lines)):
        if i not in changed_lines and a != b:
            raise HexError(f"line {i + 1} changed but holds no patched byte")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("stock_hex", type=Path, help="stock A_H_25_REV16_7.HEX")
    parser.add_argument("-o", "--output-dir", type=Path,
                        help="where to write the ESC files (default: next to the stock file)")
    args = parser.parse_args(argv)

    out_dir = args.output_dir or args.stock_hex.parent
    try:
        stock_lines = args.stock_hex.read_bytes().decode("ascii").splitlines(keepends=True)
        stock_mem = memory_map(stock_lines)
        check_stock(stock_mem)
        out_dir.mkdir(parents=True, exist_ok=True)
        for name, direction in OUTPUTS.items():
            changes = {addr: new for addr, (_, _, new) in COMMON_PATCH.items()}
            changes[DIRECTION_ADDR] = direction
            out_lines, changed = apply_patch(stock_lines, stock_mem, changes)
            verify_output(stock_mem, out_lines, changes, changed, stock_lines)
            (out_dir / name).write_bytes("".join(out_lines).encode("ascii"))
            records = ", ".join(str(i + 1) for i in changed)
            print(f"wrote {out_dir / name}: {len(changes)} bytes patched, "
                  f"records on lines {records} rechecksummed, "
                  f"{len(out_lines)} records validated")
    except (HexError, OSError, UnicodeDecodeError) as err:
        print(f"error: {err}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
