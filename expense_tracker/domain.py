from dataclasses import dataclass
from datetime import date
from decimal import Decimal, InvalidOperation
import re


def parse_amount(raw: str) -> Decimal:
    try:
        amount = Decimal(raw)
    except InvalidOperation as exc:
        raise ValueError("amount must be a positive finite decimal.") from exc
    if not amount.is_finite() or amount <= 0:
        raise ValueError("amount must be a positive finite decimal.")
    return amount


def parse_date(raw: str) -> date:
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", raw):
        raise ValueError("date must use YYYY-MM-DD")
    return date.fromisoformat(raw)


@dataclass(frozen=True)
class Summary:
    overall: Decimal
    by_category: dict[str, Decimal]


def summarize_by_category(expenses) -> Summary:
    totals: dict[str, Decimal] = {}
    for expense in expenses:
        totals[expense.category] = totals.get(expense.category, Decimal("0")) + expense.amount
    return Summary(sum(totals.values(), Decimal("0")), totals)
