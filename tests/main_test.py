from __future__ import annotations

import runpy

import pytest

from venvy.main import main


def test_dunder_main() -> None:
    with pytest.raises(SystemExit) as exc_info:
        runpy.run_module("venvy", run_name="__main__")
    assert exc_info.value.code == 0


@pytest.mark.parametrize(
    ("argv", "exit_code"), [
        ([], 0),
        (["py37"], 0),
    ],
)
def test_main_return_value(argv: list[str], exit_code: int) -> None:
    assert main(argv) == exit_code


@pytest.mark.parametrize(
    ("argv", "exit_code"), [
        (["--help"], 0),
        (["--version"], 0),
        (["--non-existent-argument"], 2),
    ],
)
def test_argparse(argv: list[str], exit_code: int) -> None:
    with pytest.raises(SystemExit):
        assert main(argv) == exit_code
