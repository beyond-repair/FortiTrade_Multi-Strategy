"""CLI / package entry smoke tests."""

import subprocess
import sys
from pathlib import Path

from fortitrade.__main__ import main

REPO = Path(__file__).resolve().parent.parent


def test_main_demo_exit_0():
    assert main(["demo", "--csv", str(REPO / "data" / "historical_data.csv")]) == 0


def test_python_m_fortitrade():
    proc = subprocess.run(
        [sys.executable, "-m", "fortitrade", "demo"],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr
    assert "Claim-0" in proc.stdout or "Decision:" in proc.stdout
