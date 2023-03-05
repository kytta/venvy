from __future__ import annotations

import os
import sys

import pytest

from venvy import parse_query
from venvy import VirtualEnvParams

TESTS_DIR = os.path.dirname(__file__)
only_on_win32 = pytest.mark.skipif(
    sys.platform != "win32",
    reason="Only runs on Windows",
)
only_on_nix = pytest.mark.skipif(
    sys.platform == "win32",
    reason="Only runs on non-Windows OS",
)

# TODO: update derived activators when we detect activators


@pytest.mark.parametrize(
    ("query", "expected"), [
        ([], (None, ".venv", {"bash"})),
        (["37"], ("37", ".venv", {"bash"})),
        (["csh", "3.7"], ("3.7", ".venv", {"bash", "cshell"})),
        (["pypy", "myvenv"], ("pypy", "myvenv", {"bash"})),
        (
            [os.path.join(TESTS_DIR, "resources", "executable")],
            (
                os.path.join(
                    TESTS_DIR, "resources",
                    "executable",
                ), ".venv", {"bash"},
            ),
        ),
    ],
)
def test_parse_query(
    query: list[str],
    expected: tuple[str | None, str, set[str]],
    monkeypatch,
) -> None:
    import shellingham

    def return_bash():
        return "bash", "/bin/bash"

    monkeypatch.setattr(shellingham, "detect_shell", return_bash)
    assert parse_query(query) == VirtualEnvParams(*expected)


def test_parse_query_in_unsupported_shell(monkeypatch) -> None:
    import shellingham

    def return_xonsh():
        return "xonsh", "/usr/local/bin/xonsh"

    monkeypatch.setattr(shellingham, "detect_shell", return_xonsh)
    assert parse_query([]) == VirtualEnvParams(None, ".venv", set())
