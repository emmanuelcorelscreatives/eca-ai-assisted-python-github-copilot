"""Shared rules from the saved expense data contract and lesson 71 example."""
from dataclasses import dataclass
from datetime import date
from decimal import Decimal, localcontext
import re


CATEGORY_PROFILES = {
    "contract": frozenset({"food", "transport", "housing", "utilities", "health", "entertainment", "other"}),
    "lesson71": frozenset({"groceries", "transit"}),
}


class ExpenseValidationError(ValueError):
    pass


@dataclass(frozen=True)
class ExpenseDraft:
    amount_minor: int
    spent_on: str
    category: str
    description: str | None


@dataclass(frozen=True)
class Expense:
    id: int
    amount_minor: int
    spent_on: str
    category: str
    description: str | None


def parse_amount(raw: str) -> int:
    if not re.fullmatch(r"[0-9]+(?:\.[0-9]{1,2})?", raw):
        raise ExpenseValidationError("amount must contain digits and at most two decimal places")
    value = Decimal(raw)
    if not value.is_finite() or value <= 0:
        raise ExpenseValidationError("amount must be greater than zero and finite")
    with localcontext() as context:
        context.prec = max(28, len(value.as_tuple().digits) + 3)
        return int(value * 100)


def parse_day(raw: str) -> date:
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", raw):
        raise ExpenseValidationError("date must use YYYY-MM-DD")
    try:
        return date.fromisoformat(raw)
    except ValueError as error:
        raise ExpenseValidationError("date must be a real calendar date") from error


def validate_category(raw: str, profile: str) -> str:
    category = raw.strip()
    if category not in CATEGORY_PROFILES[profile]:
        raise ExpenseValidationError("category must be one of: " + ", ".join(sorted(CATEGORY_PROFILES[profile])))
    return category


def validate_expense(amount: str, spent_on: str, category: str, description: str | None,
                     *, current_day: date, profile: str = "contract") -> ExpenseDraft:
    minor = parse_amount(amount)
    day = parse_day(spent_on)
    if day > current_day:
        raise ExpenseValidationError("date must not be in the future")
    normalized_category = validate_category(category, profile)
    if description is not None and len(description) > 200:
        raise ExpenseValidationError("description must be at most 200 characters")
    return ExpenseDraft(minor, day.isoformat(), normalized_category,
                        description if description and description.strip() else None)


def validate_filters(start: str | None, end: str | None, category: str | None,
                     profile: str) -> tuple[str | None, str | None, str | None]:
    first = parse_day(start).isoformat() if start is not None else None
    last = parse_day(end).isoformat() if end is not None else None
    if first is not None and last is not None and first > last:
        raise ExpenseValidationError("start date must not be after end date")
    return first, last, validate_category(category, profile) if category is not None else None


def validate_id(expense_id: int) -> None:
    if type(expense_id) is not int or expense_id <= 0:
        raise ExpenseValidationError("id must be a positive integer")


def format_amount(amount_minor: int) -> str:
    whole, cents = divmod(amount_minor, 100)
    return f"{whole}.{cents:02d}"


def summarize(expenses: list[Expense]) -> tuple[int, dict[str, int]]:
    totals: dict[str, int] = {}
    for expense in expenses:
        totals[expense.category] = totals.get(expense.category, 0) + expense.amount_minor
    return sum(totals.values()), totals
