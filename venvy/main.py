from __future__ import annotations

import argparse
import sys
from typing import Sequence

if sys.version_info < (3, 8):
    from importlib_metadata import version
else:
    from importlib.metadata import version


def _get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="A very opinionated virtualenv wrapper for an even "
                    "simpler venv management.",
    )
    parser.add_argument(
        "-V", "--version",
        action="version",
        version=version("venvy"),
    )

    parser.add_argument(
        "query",
        type=str,
        nargs="*",
        default=[".venv"],
        metavar="QUERY",
        help="Magic query argument. Allows you to specify the name, the "
             "Python distribution or version, or everything at once.",
    )

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]

    args = _get_parser().parse_args(argv)
    print(args)

    return 1
