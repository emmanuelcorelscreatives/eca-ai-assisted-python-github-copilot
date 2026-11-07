from datetime import date
from decimal import Decimal, InvalidOperation


def amount_minor_units(raw: str) -> int:
    try:
        amount = Decimal(raw)
    except InvalidOperation as exc:
        raise ValueError('Enter a decimal amount') from exc

    cents = amount * 100
    if not amount.is_finite() or amount < 0 or cents != cents.to_integral_value():
        raise ValueError('Enter a nonnegative amount with at most two decimal places')
    return int(cents)


def is_valid_date(raw: str) -> bool:
    try:
        date.fromisoformat(raw)
    except ValueError:
        return False
    return True


def summarize_expenses(
    entries: list[tuple[str, int]],
) -> tuple[int, dict[str, int]]:
    by_category: dict[str, int] = {}
    overall = 0
    for category, cents in entries:
        overall += cents
        by_category[category] = by_category.get(category, 0) + cents
    return overall, by_category
