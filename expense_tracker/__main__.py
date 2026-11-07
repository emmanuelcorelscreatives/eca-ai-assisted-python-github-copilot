import argparse
import sys
from .domain import parse_amount, parse_date
from .models import NewExpense
from .repository import SQLiteExpenseRepository


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--database", default="expenses.db")
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("add")
    add.add_argument("--amount", required=True)
    add.add_argument("--date", required=True)
    add.add_argument("--category", required=True)
    add.add_argument("--description", required=True)
    commands.add_parser("list")
    args = parser.parse_args()
    if args.command == "add":
        try:
            expense = NewExpense(amount=parse_amount(args.amount), spent_on=parse_date(args.date), category=args.category, description=args.description)
        except ValueError as exc:
            print(f"Error: {exc}", file=sys.stderr)
            return 2
        repository = SQLiteExpenseRepository(args.database)
        try:
            saved = repository.add(expense)
            print(f"Added expense {saved.id}.")
        finally:
            repository.close()
    else:
        repository = SQLiteExpenseRepository(args.database)
        try:
            expenses = repository.list_all()
            if not expenses:
                print("No expenses found.")
            for expense in expenses:
                print(f"{expense.id} | {expense.spent_on.isoformat()} | {expense.category} | {expense.amount:.2f} | {expense.description}")
        finally:
            repository.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
