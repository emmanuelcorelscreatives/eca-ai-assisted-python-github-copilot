from decimal import Decimal

from expense_tracker.summary import calculate_total


def test_calculate_total_includes_every_expense() -> None:
    amounts = [Decimal("10.00"), Decimal("2.50")]

    result = calculate_total(amounts)

    assert result == Decimal("12.50")
