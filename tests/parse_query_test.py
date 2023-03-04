from __future__ import annotations

import os
import sys
from typing import Sequence

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
        ([], (None, ".venv", [])),
        (["37"], ("37", ".venv", [])),
        (["bash", "3.7"], ("3.7", ".venv", ["bash"])),
        (["pypy", "myvenv"], ("pypy", "myvenv", [])),
        (
            [os.path.join(TESTS_DIR, "resources", "executable")],
            (os.path.join(TESTS_DIR, "resources", "executable"), ".venv", []),
        ),
    ],
)
def test_parse_query(
    query: list[str],
    expected: tuple[str | None, str, Sequence[str]],
) -> None:
    assert parse_query(query) == VirtualEnvParams(*expected)
