#!/usr/bin/env python3
from pathlib import Path
import shutil, sys

ROOT = Path(__file__).resolve().parents[1]
PAIRS = [
    (ROOT/'kernel/bootstrap.txt', ROOT/'docs/canonical/bootstrap.txt'),
    (ROOT/'kernel/current.json', ROOT/'docs/canonical/current.json'),
    (ROOT/'state/current.json', ROOT/'docs/canonical/state.json'),
]

def main():
    check = '--check' in sys.argv
    bad = []
    for src, dst in PAIRS:
        if check:
            if not dst.exists() or src.read_bytes() != dst.read_bytes():
                bad.append(f'{dst.relative_to(ROOT)} != {src.relative_to(ROOT)}')
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
    if check and bad:
        print('Public mirror drift:')
        for item in bad: print(' -', item)
        raise SystemExit(1)
    print('Public canonical mirror OK' if check else 'Public canonical mirror synchronized')

if __name__ == '__main__':
    main()
