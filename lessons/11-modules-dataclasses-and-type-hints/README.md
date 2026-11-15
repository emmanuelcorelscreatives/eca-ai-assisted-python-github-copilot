# 11. Modules, Dataclasses and Type Hints

Emmanuel Corels Academy

Organize imports and define an expense-record representation while explaining that type annotations do not validate runtime input.

[Course repository](https://github.com/emmanuelcorelscreatives/eca-ai-assisted-python-github-copilot)

Inspect the root `expense_tracker/models.py`. In a disposable scratch file,
import `NewExpense`, `date` and `Decimal`, then construct
`NewExpense(Decimal("12.50"), date(2025, 3, 8), "food", "Lunch")`.
Predict its `amount` and `spent_on` types. Compare its fields with `Expense`:
the saved record additionally has an `id`. Both dataclasses are frozen; trying
to assign another amount raises `dataclasses.FrozenInstanceError`.
Explain why a type hint alone does not validate incoming user text. Trace the
real import and validation boundary in `expense_tracker/__main__.py`; do not
replace these models with a different lesson's standalone schema.
