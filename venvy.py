from __future__ import annotations

import argparse
import contextlib
import os.path
import re
import sys
from importlib.metadata import version
from typing import NamedTuple
from typing import Sequence

from virtualenv import cli_run
from virtualenv.run.plugin.base import PluginLoader


class VirtualEnvParams(NamedTuple):
    python: str | None         # Python definition
    dest: str                  # folder name of the virtualenv
    activators: set[str]  # list of activators to enable


# Partly taken from virtualenv:
# https://github.com/pypa/virtualenv/blob/e7fa1c2b4bbbe7495077e5f2146dca9c369b08d7/src/virtualenv/discovery/py_spec.py#L9
PY_TAG_RE = re.compile(
    r"^(?P<implementation>py(thon)?|cp(ython)?|ip|pp|pypy|jy(thon)?)?"
    r"(?P<version>[0-9.]+)?"
    r"(?:-(?P<arch>32|64))?$",
)

ACTIVATOR_ALIASES: dict[str, list[str]] = {
    "bash": ["ash", "dash", "ksh", "sh", "shell", "zsh"],
    "batch": ["bat", "cmd"],
    "cshell": ["csh", "tcsh"],
    "fish": [],
    "nushell": ["nu"],
    "powershell": ["ps1", "pwsh"],
    "python": ["py"],
}


def get_activator_map() -> dict[str, str]:
    entry_points = PluginLoader.entry_points_for("virtualenv.activate")
    activators = {key: key for key in entry_points}

    for activator in entry_points:
        for alias in ACTIVATOR_ALIASES.get(activator, []):
            activators[alias] = activator

    return activators


def parse_query(query: list[str]) -> VirtualEnvParams:
    python: str | None = None
    dest: str = ".venv"
    activators: set[str] = set()
    activator_map = get_activator_map()

    for part in query:
        if not python:
            version_match = PY_TAG_RE.match(part)
            if version_match:
                python = version_match.group()
                continue

        if part in activator_map:
            activators.add(activator_map[part])
            continue

        if os.path.isfile(part) and os.access(part, os.X_OK):
            # probably a python executable?
            python = part
            continue

        # probably a venv name
        dest = part
        continue

    import shellingham
    with contextlib.suppress(shellingham.ShellDetectionFailure):
        current_shell = shellingham.detect_shell()[0]
        if current_shell in activator_map:
            activators.add(activator_map[current_shell])

    return VirtualEnvParams(
        python=python,
        dest=dest,
        activators=activators,
    )


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
    params = parse_query(args.query)

    virtualenv_args = [
        "--download",
    ]
    if params.python:
        virtualenv_args.extend(["--python", params.python])
    if params.activators:
        virtualenv_args.extend(["--activators", ",".join(params.activators)])
    virtualenv_args.append(params.dest)

    cli_run(virtualenv_args)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
