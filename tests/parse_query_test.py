from __future__ import annotations

import os
from typing import Sequence

import pytest

from venvy import parse_query
from venvy import VirtualEnvParams

TESTS_DIR = os.path.dirname(__file__)

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
