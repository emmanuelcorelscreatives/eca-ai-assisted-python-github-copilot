"""Coordinate validation before opening storage or writing an expense."""
from datetime import date

from .domain import summarize, validate_expense, validate_filters, validate_id
from .sqlite_repository import SQLiteExpenseRepository


def add_expense(database_path, amount, spent_on, category, description=None, *, current_day=None, profile="contract"):
    draft = validate_expense(amount, spent_on, category, description,
                             current_day=current_day if current_day is not None else date.today(), profile=profile)
    with SQLiteExpenseRepository(database_path) as repository:
        return repository.add(draft)


def list_expenses(database_path, *, start=None, end=None, category=None, profile="contract"):
    first, last, normalized_category = validate_filters(start, end, category, profile)
    with SQLiteExpenseRepository(database_path) as repository:
        return repository.list_all(start=first, end=last, category=normalized_category)


def summarize_expenses(database_path, **filters):
    return summarize(list_expenses(database_path, **filters))


def delete_expense(database_path, expense_id):
    validate_id(expense_id)
    with SQLiteExpenseRepository(database_path) as repository:
        return repository.delete(expense_id)
