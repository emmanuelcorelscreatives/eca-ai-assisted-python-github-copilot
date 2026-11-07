from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass(frozen=True)
class NewExpense:
    amount: Decimal
    spent_on: date
    category: str
    description: str


@dataclass(frozen=True)
class Expense:
    id: int | None
    amount: Decimal
    spent_on: date
    category: str
    description: str
