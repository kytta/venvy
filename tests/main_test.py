from __future__ import annotations

import pytest

from venvy import main


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
