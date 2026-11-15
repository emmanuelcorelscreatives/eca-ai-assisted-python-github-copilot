from datetime import date
from decimal import Decimal, InvalidOperation
import re


def amount_minor_units(raw: str) -> int:
    if not re.fullmatch(r"[0-9]+(?:\.[0-9]{1,2})?", raw):
        raise ValueError('Enter a positive amount with at most two decimal places')
    try:
        amount = Decimal(raw)
    except InvalidOperation as exc:
        raise ValueError('Enter a decimal amount') from exc

    if not amount.is_finite() or amount <= 0:
        raise ValueError('Enter a positive amount with at most two decimal places')
    cents = amount * 100
    return int(cents)


def is_valid_date(raw: str) -> bool:
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", raw):
        return False
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
