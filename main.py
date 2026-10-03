"""Display Scale Set — Set Windows display scaling to 100, 125, or 150 for the current monitor when the API allows it."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='display_scale_set',
        description='Set Windows display scaling to 100, 125, or 150 for the current monitor when the API allows it.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Display Scale Set')
    print('Scaling without the Settings hunt.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
