from __future__ import annotations

import argparse
import sys
from typing import Sequence


def _get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    return 0


if __name__ == "__main_":
    raise SystemExit(main())
