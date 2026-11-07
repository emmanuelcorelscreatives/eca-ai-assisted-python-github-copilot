from datetime import date
from decimal import Decimal

from expense_tracker.models import NewExpense
from expense_tracker.repository import SQLiteExpenseRepository


def test_expense_survives_repository_reopen(tmp_path):
    db_path = tmp_path / "expenses.db"

    writer = SQLiteExpenseRepository(db_path)
    try:
        saved = writer.add(
            NewExpense(
                amount=Decimal("12.50"),
                spent_on=date(2025, 3, 8),
                category="food",
                description="Lunch",
            )
        )
        saved_id = saved.id
    finally:
        writer.close()

    assert saved_id is not None

    reader = SQLiteExpenseRepository(db_path)
    try:
        loaded = reader.get(saved_id)
    finally:
        reader.close()

    assert loaded is not None
    assert loaded.id == saved_id
    assert loaded.amount == Decimal("12.50")
    assert loaded.spent_on == date(2025, 3, 8)
    assert loaded.category == "food"
    assert loaded.description == "Lunch"
