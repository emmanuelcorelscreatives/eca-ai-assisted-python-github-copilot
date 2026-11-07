"""Arguments and presentation; domain and storage rules stay in their layers."""
import argparse
import sqlite3
import sys

from . import service
from .domain import CATEGORY_PROFILES, ExpenseValidationError, format_amount


def main(argv=None):
    parser = argparse.ArgumentParser(description="Emmanuel Corels Academy capstone expense tracker")
    parser.add_argument("--database", default="expenses.db")
    parser.add_argument("--category-profile", choices=sorted(CATEGORY_PROFILES), default="contract")
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("add")
    add.add_argument("--amount", required=True)
    add.add_argument("--date", required=True)
    add.add_argument("--category", required=True)
    add.add_argument("--description")
    for name in ("list", "summary"):
        command = commands.add_parser(name)
        command.add_argument("--start")
        command.add_argument("--end")
        command.add_argument("--category")
    delete = commands.add_parser("delete")
    delete.add_argument("id", type=int)
    args = parser.parse_args(argv)
    try:
        if args.command == "add":
            saved = service.add_expense(args.database, args.amount, args.date, args.category,
                                        args.description, profile=args.category_profile)
            print(f"Added expense {saved.id}.")
        elif args.command in ("list", "summary"):
            filters = dict(start=args.start, end=args.end, category=args.category, profile=args.category_profile)
            if args.command == "list":
                rows = service.list_expenses(args.database, **filters)
                if not rows:
                    print("No expenses match those filters.")
                for expense in rows:
                    print(f"{expense.id} | {expense.spent_on} | {expense.category} | {format_amount(expense.amount_minor)} | {expense.description or ''}")
            else:
                overall, categories = service.summarize_expenses(args.database, **filters)
                print(f"Overall: {format_amount(overall)}")
                for category, amount in sorted(categories.items()):
                    print(f"{category}: {format_amount(amount)}")
        else:
            if not service.delete_expense(args.database, args.id):
                print(f"Expense {args.id} was not found.", file=sys.stderr)
                return 1
            print(f"Deleted expense {args.id}.")
    except ExpenseValidationError as error:
        print(f"Validation error: {error}", file=sys.stderr)
        return 2
    except (sqlite3.Error, OSError, OverflowError) as error:
        print(f"Storage error: {error}", file=sys.stderr)
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
