from __future__ import annotations

import pytest

from venvy import main


@pytest.mark.parametrize(
    ("argv", "exit_code"), [
        ([], 0),
        (["py37"], 0),
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
