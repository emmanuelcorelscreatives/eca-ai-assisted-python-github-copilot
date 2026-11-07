from datetime import date
import json
from pathlib import Path
import sqlite3
import subprocess
import sys

import pytest

from expense_tracker import service
from expense_tracker.cli import main
from expense_tracker.domain import ExpenseDraft, ExpenseValidationError, parse_amount, validate_expense
from expense_tracker.sqlite_repository import SQLiteExpenseRepository


TODAY = date(2026, 4, 15)


@pytest.mark.parametrize("raw, expected", [("12", 1200), ("12.3", 1230), ("12.30", 1230), ("0.01", 1)])
def test_exact_minor_units(raw, expected):
    assert parse_amount(raw) == expected


@pytest.mark.parametrize("raw", ["$12.30", "1,000.00", "1e2", "NaN", "Infinity", "0", "-2.50", "12.345", "12.300"])
def test_rejected_amount_never_opens_repository(monkeypatch, raw):
    def forbidden(*_):
        pytest.fail("invalid input reached storage")
    monkeypatch.setattr(service, "SQLiteExpenseRepository", forbidden)
    with pytest.raises(ExpenseValidationError, match="amount"):
        service.add_expense("unused.db", raw, "2026-04-15", "food", current_day=TODAY)


def test_date_category_and_description_boundaries():
    valid = validate_expense("12.30", "2026-04-15", " food ", "x" * 200, current_day=TODAY)
    assert valid == ExpenseDraft(1230, "2026-04-15", "food", "x" * 200)
    assert validate_expense("1", "2026-04-15", "food", "  ", current_day=TODAY).description is None
    for day in ("2026-04-16", "2026-02-30", "04/15/2026", "2026-04-15T12:00:00"):
        with pytest.raises(ExpenseValidationError, match="date"):
            validate_expense("1", day, "food", "", current_day=TODAY)
    for category in ("Food", "", " ", "groceries"):
        with pytest.raises(ExpenseValidationError, match="category"):
            validate_expense("1", "2026-04-15", category, "", current_day=TODAY)
    with pytest.raises(ExpenseValidationError, match="description"):
        validate_expense("1", "2026-04-15", "food", "x" * 201, current_day=TODAY)


def test_lesson71_profile_is_explicit_and_not_a_category_alias():
    draft = validate_expense("12.40", "2025-04-12", "groceries", "bread", current_day=TODAY, profile="lesson71")
    assert draft.category == "groceries"
    with pytest.raises(ExpenseValidationError, match="category"):
        validate_expense("1", "2025-04-12", "food", "", current_day=TODAY, profile="lesson71")


def test_duplicates_are_distinct_and_restart_reads_disk(tmp_path):
    path = str(tmp_path / "expenses.db")
    first = service.add_expense(path, "12.30", "2026-04-15", "food", "a", current_day=TODAY)
    second = service.add_expense(path, "12.30", "2026-04-15", "food", "a", current_day=TODAY)
    assert first.id > 0 and second.id > 0 and first.id != second.id
    with SQLiteExpenseRepository(path) as reopened:
        assert reopened.list_all() == [first, second]


def test_inclusive_date_filters_and_reversed_range(tmp_path):
    path = str(tmp_path / "expenses.db")
    first = service.add_expense(path, "12.30", "2026-04-14", "food", current_day=TODAY)
    second = service.add_expense(path, "4", "2026-04-15", "transport", current_day=TODAY)
    assert service.list_expenses(path, start="2026-04-14", end="2026-04-14") == [first]
    assert service.list_expenses(path, start="2026-04-14", end="2026-04-15") == [first, second]
    assert service.list_expenses(path, category="transport") == [second]
    with pytest.raises(ExpenseValidationError, match="start date"):
        service.list_expenses(path, start="2026-04-15", end="2026-04-14")


def test_delete_only_selected_id_and_preserve_others(tmp_path):
    path = str(tmp_path / "expenses.db")
    first = service.add_expense(path, "12.30", "2026-04-15", "food", current_day=TODAY)
    second = service.add_expense(path, "4", "2026-04-15", "transport", current_day=TODAY)
    assert service.delete_expense(path, first.id) is True
    assert service.delete_expense(path, first.id) is False
    assert service.list_expenses(path) == [second]
    with SQLiteExpenseRepository(path) as repository:
        for identifier in (0, -1, True, "1"):
            with pytest.raises(ExpenseValidationError, match="positive integer"):
                repository.delete(identifier)


def test_failed_real_sqlite_commit_rolls_back_and_returns_no_success(tmp_path):
    path = str(tmp_path / "expenses.db")
    with SQLiteExpenseRepository(path) as repository:
        repository.connection.execute("PRAGMA foreign_keys = ON")
        repository.connection.executescript("""
            CREATE TABLE parent (id INTEGER PRIMARY KEY);
            CREATE TABLE child (parent_id INTEGER REFERENCES parent(id) DEFERRABLE INITIALLY DEFERRED);
            CREATE TRIGGER fail_at_commit AFTER INSERT ON expenses
            BEGIN INSERT INTO child (parent_id) VALUES (999); END;
        """)
        with pytest.raises(sqlite3.IntegrityError):
            repository.add(ExpenseDraft(1230, "2026-04-15", "food", ""))
        assert repository.list_all() == []


def test_storage_open_error_is_not_missing_or_success(tmp_path, capsys):
    missing_parent = str(tmp_path / "absent" / "expenses.db")
    assert main(["--database", missing_parent, "delete", "1"]) == 3
    output = capsys.readouterr()
    assert output.out == ""
    assert "Storage error:" in output.err and "not found" not in output.err
    assert main(["--database", missing_parent, "add", "--amount", "1", "--date", "2025-04-12", "--category", "food"]) == 3
    assert capsys.readouterr().out == ""


def test_sql_parameters_preserve_description_and_table(tmp_path):
    path = str(tmp_path / "expenses.db")
    payload = "'); DROP TABLE expenses; --"
    expense = service.add_expense(path, "1", "2026-04-15", "food", payload, current_day=TODAY)
    assert service.list_expenses(path) == [expense]


def test_exact_lesson71_sequence_across_independent_processes(tmp_path):
    path = str(tmp_path / "lesson71.db")
    directory = Path(__file__).resolve().parents[1]

    def run(*args, code=0):
        result = subprocess.run([sys.executable, "-m", "expense_tracker", "--database", path,
                                 "--category-profile", "lesson71", *args], cwd=directory,
                                capture_output=True, text=True)
        assert result.returncode == code, result.stderr
        return result

    assert run("list").stdout == "No expenses match those filters.\n"
    ids = []
    for day, amount, category, description in [("2025-04-12", "12.40", "groceries", "bread"),
                                                ("2025-04-13", "7.60", "groceries", "milk"),
                                                ("2025-04-14", "5.25", "transit", "bus")]:
        result = run("add", "--date", day, "--amount", amount, "--category", category, "--description", description)
        ids.append(int(result.stdout.removeprefix("Added expense ").strip().rstrip(".")))
    assert len(set(ids)) == 3
    all_rows = run("list").stdout
    assert len(all_rows.splitlines()) == 3
    groceries = run("list", "--category", "groceries").stdout
    assert "bread" in groceries and "milk" in groceries and "bus" not in groceries
    transit = run("list", "--category", "transit").stdout
    assert "bus" in transit and "bread" not in transit and "milk" not in transit
    assert run("summary").stdout == "Overall: 25.25\ngroceries: 20.00\ntransit: 5.25\n"
    invalid = run("add", "--date", "2025-04-12", "--amount", "not-a-number", "--category", "groceries", code=2)
    assert invalid.stdout == "" and "amount" in invalid.stderr
    assert run("list").stdout == all_rows
    run("delete", str(ids[1]))
    remaining = run("list").stdout
    assert "bread" in remaining and "bus" in remaining and "milk" not in remaining
    assert run("summary").stdout == "Overall: 17.65\ngroceries: 12.40\ntransit: 5.25\n"
    assert run("list").stdout == remaining
    run("delete", str(ids[1]), code=1)
    run("delete", "0", code=2)
