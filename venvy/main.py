from __future__ import annotations

import argparse
import os.path
import re
import sys
from typing import NamedTuple
from typing import Sequence

if sys.version_info < (3, 8):  # pragma: <3.8 cover
    from importlib_metadata import version
else:  # pragma: >=3.8 cover
    from importlib.metadata import version


class VirtualEnvParams(NamedTuple):
    python: str                # Python definition
    dest: str                  # folder name of the virtualenv
    activators: Sequence[str]  # list of activators to enable


# Partly taken from virtualenv:
# https://github.com/pypa/virtualenv/blob/e7fa1c2b4bbbe7495077e5f2146dca9c369b08d7/src/virtualenv/discovery/py_spec.py#L9
PY_TAG_RE = re.compile(
    r"^(?P<implementation>py(thon)?|cp(ython)?|ip|pp|pypy|jy(thon)?)?"
    r"(?P<version>[0-9.]+)?"
    r"(?:-(?P<arch>32|64))?$",
)
SHELL_NAME_RE = re.compile(
    r"^(a|ba|c|da|fi|z)sh|(c|nu|power)shell|ps1|python$",
    flags=re.I,
)


def parse_query(query: list[str]) -> VirtualEnvParams:
    python: str = ""
    dest: str = ".venv"
    activators: list[str] = []

    for part in query:
        if not python:
            version_match = PY_TAG_RE.match(part)
            if version_match:
                python = version_match.group()
                continue

        shell_match = SHELL_NAME_RE.match(part)
        if shell_match:
            activator = None
            shell = shell_match.group()
            if shell in ["ash", "bash", "dash", "zsh"]:
                activator = "bash"  # POSIX
            elif shell in ["csh", "cshell"]:
                activator = "cshell"  # CShell
            elif shell in ["powershell", "ps1"]:
                activator = "powershell"  # PowerShell
            elif shell in ["fish", "nushell", "python"]:
                activator = shell
            else:
                continue

            activators.append(activator)
            continue

        if os.path.exists(part):
            # probably a python executable?
            python = part
            continue
        else:
            # probably a venv name
            dest = part
            continue

    return VirtualEnvParams(python, dest, activators)


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

    params = parse_query(args.query)

    from pprint import pprint
    pprint(params)

    return 0
