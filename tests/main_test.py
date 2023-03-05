from __future__ import annotations

import sys

import pytest

from venvy import main

CURRENT_PYTHON = f"{sys.version_info[0]}.{sys.version_info[1]}"


@pytest.mark.parametrize(
    ("argv", "exit_code"), [
        ([], 0),
        ([f"python{CURRENT_PYTHON}"], 0),
    ],
)
@pytest.mark.parametrize(
    "shell", [
        "bash",
        "xonsh",
    ],
)
def test_main_return_value(
    argv: list[str],
    exit_code: int,
    shell: str,
    monkeypatch,
) -> None:
    import shellingham

    def return_shell():
        return shell, f"/usr/local/bin/{shell}"

    monkeypatch.setattr(shellingham, "detect_shell", return_shell)
    assert main(argv) == exit_code
