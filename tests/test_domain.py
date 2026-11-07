from datetime import date
from decimal import Decimal

import pytest

from expense_tracker.domain import parse_amount, parse_date, summarize_by_category
from expense_tracker.models import Expense


def test_parse_amount_accepts_smallest_valid_amount():
    assert parse_amount("0.01") == Decimal("0.01")


@pytest.mark.parametrize("raw", ["0", "-0.01", "NaN", "Infinity"])
def test_parse_amount_rejects_non_positive_or_non_finite_values(raw):
    with pytest.raises(ValueError):
        parse_amount(raw)


def test_parse_date_accepts_real_leap_day():
    assert parse_date("2024-02-29") == date(2024, 2, 29)


@pytest.mark.parametrize("raw", ["2025-02-29", "03/08/2025"])
def test_parse_date_rejects_invalid_or_ambiguous_dates(raw):
    with pytest.raises(ValueError):
        parse_date(raw)


def test_summarize_uses_independently_derived_expected_totals():
    expenses = [
        Expense(
            id=1,
            amount=Decimal("4.25"),
            spent_on=date(2025, 3, 8),
            category="food",
            description="Breakfast",
        ),
        Expense(
            id=2,
            amount=Decimal("6.00"),
            spent_on=date(2025, 3, 8),
            category="food",
            description="Lunch",
        ),
        Expense(
            id=3,
            amount=Decimal("2.75"),
            spent_on=date(2025, 3, 9),
            category="travel",
            description="Bus",
        ),
    ]

    summary = summarize_by_category(expenses)

    assert summary.overall == Decimal("13.00")
    assert summary.by_category == {
        "food": Decimal("10.25"),
        "travel": Decimal("2.75"),
    }
