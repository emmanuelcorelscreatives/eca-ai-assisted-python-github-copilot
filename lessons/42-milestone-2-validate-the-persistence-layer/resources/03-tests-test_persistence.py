from pathlib import Path
import subprocess
import sys

import pytest

from expense_store import ExpenseStore


def test_creation_reads_back_complete_row(db_path):
    store = ExpenseStore(db_path)
    expense_id = store.add('12.50', '2025-03-01', 'food')

    assert store.list() == [(expense_id, '12.50', '2025-03-01', 'food')]


def test_filter_returns_only_matching_rows_in_order(db_path):
    store = ExpenseStore(db_path)
    first_id = store.add('8.00', '2025-03-01', 'travel')
    store.add('12.50', '2025-03-02', 'food')
    last_id = store.add('3.25', '2025-03-03', 'travel')

    assert store.list(category='travel') == [
        (first_id, '8.00', '2025-03-01', 'travel'),
        (last_id, '3.25', '2025-03-03', 'travel'),
    ]
    assert store.list(category='books') == []


def test_delete_targets_one_id_and_reports_missing(db_path):
    store = ExpenseStore(db_path)
    food_id = store.add('12.50', '2025-03-01', 'food')
    travel_id = store.add('8.00', '2025-03-02', 'travel')
    surviving_row = (travel_id, '8.00', '2025-03-02', 'travel')

    assert store.delete(food_id) is True
    assert store.list() == [surviving_row]
    assert store.delete(food_id) is False
    assert store.list() == [surviving_row]


@pytest.mark.parametrize(
    'invalid_expense',
    [
        ('NaN', '2025-03-01', 'food'),
        ('12.00', '2025-02-30', 'food'),
        ('12.00', '2025-03-01', ' '),
    ],
)
def test_invalid_add_leaves_existing_storage_unchanged(db_path, invalid_expense):
    store = ExpenseStore(db_path)
    existing_id = store.add('4.75', '2025-03-01', 'travel')
    expected = [(existing_id, '4.75', '2025-03-01', 'travel')]

    with pytest.raises(ValueError):
        store.add(*invalid_expense)

    assert store.list() == expected
    assert ExpenseStore(db_path).list() == expected


def test_surviving_record_persists_in_new_process(db_path):
    store = ExpenseStore(db_path)
    removed_id = store.add('8.00', '2025-03-01', 'travel')
    surviving_id = store.add('12.50', '2025-03-02', 'food')
    assert store.delete(removed_id) is True

    child_code = (
        'import sys; from expense_store import ExpenseStore; '
        "[print(*row, sep='|') for row in ExpenseStore(sys.argv[1]).list()]"
    )
    result = subprocess.run(
        [sys.executable, '-c', child_code, str(db_path)],
        cwd=Path(__file__).resolve().parents[1],
        capture_output=True,
        text=True,
        check=True,
    )

    assert result.stdout == f'{surviving_id}|12.50|2025-03-02|food\n'
    assert result.stderr == ''


def test_separate_database_paths_do_not_share_rows(db_path):
    other_path = db_path.with_name('other.sqlite3')
    try:
        first = ExpenseStore(db_path)
        second = ExpenseStore(other_path)
        first_id = first.add('5.00', '2025-03-01', 'food')
        first_row = (first_id, '5.00', '2025-03-01', 'food')

        assert second.list() == []
        second_id = second.add('7.00', '2025-03-02', 'travel')
        assert first.list() == [first_row]
        assert second.list() == [
            (second_id, '7.00', '2025-03-02', 'travel')
        ]
    finally:
        other_path.unlink(missing_ok=True)


def test_explicit_path_creates_no_other_file_in_working_directory(
    db_path, tmp_path, monkeypatch
):
    monkeypatch.chdir(tmp_path)
    store = ExpenseStore(db_path)
    store.add('2.00', '2025-03-01', 'food')

    assert {path.name for path in tmp_path.iterdir()} == {'expenses.sqlite3'}
