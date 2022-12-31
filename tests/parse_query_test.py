from __future__ import annotations

from typing import Sequence

import pytest

from venvy.main import parse_query
from venvy.main import VirtualEnvParams


# TODO: update derived activators when we detect activators
@pytest.mark.parametrize(
    ("query", "expected"), [
        ([], (None, ".venv", [])),
        (["37"], ("37", ".venv", [])),
        (["bash", "3.7"], ("3.7", ".venv", ["bash"])),
        (["pypy", "myvenv"], ("pypy", "myvenv", [])),
        ([__file__], (__file__, ".venv", [])),
    ],
)
def test_parse_query(
    query: list[str],
    expected: tuple[str | None, str, Sequence[str]],
) -> None:
    assert parse_query(query) == VirtualEnvParams(*expected)
