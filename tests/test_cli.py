from pathlib import Path
import subprocess
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def run_cli(db_path, *arguments):
    return subprocess.run(
        [
            sys.executable,
            "-m",
            "expense_tracker",
            "--database",
            str(db_path),
            *arguments,
        ],
        cwd=PROJECT_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def test_add_then_list_end_to_end(tmp_path):
    db_path = tmp_path / "expenses.db"

    added = run_cli(
        db_path,
        "add",
        "--amount",
        "12.50",
        "--date",
        "2025-03-08",
        "--category",
        "food",
        "--description",
        "Lunch",
    )

    assert added.returncode == 0
    assert added.stdout == "Added expense 1.\n"
    assert added.stderr == ""

    listed = run_cli(db_path, "list")

    assert listed.returncode == 0
    assert listed.stdout == "1 | 2025-03-08 | food | 12.50 | Lunch\n"
    assert listed.stderr == ""


def test_invalid_amount_reports_error_without_writing(tmp_path):
    db_path = tmp_path / "expenses.db"

    rejected = run_cli(
        db_path,
        "add",
        "--amount",
        "0",
        "--date",
        "2025-03-08",
        "--category",
        "food",
        "--description",
        "Lunch",
    )

    assert rejected.returncode == 2
    assert rejected.stdout == ""
    assert rejected.stderr == "Error: amount must be a positive finite decimal.\n"

    listed = run_cli(db_path, "list")

    assert listed.returncode == 0
    assert listed.stdout == "No expenses found.\n"
    assert listed.stderr == ""
