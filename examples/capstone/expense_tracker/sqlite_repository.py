"""Parameterized SQLite operations; report success only after commit."""
import sqlite3

from .domain import Expense, ExpenseDraft, validate_id


class SQLiteExpenseRepository:
    def __init__(self, database_path: str):
        self.connection = sqlite3.connect(database_path)
        self.connection.row_factory = sqlite3.Row
        try:
            with self.connection:
                self.connection.execute("""
                    CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY CHECK (id > 0),
                        amount_minor INTEGER NOT NULL CHECK (amount_minor > 0),
                        spent_on TEXT NOT NULL,
                        category TEXT NOT NULL,
                        description TEXT
                    )
                """)
        except BaseException:
            self.connection.close()
            raise

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.connection.close()

    def add(self, draft: ExpenseDraft) -> Expense:
        with self.connection:
            cursor = self.connection.execute(
                "INSERT INTO expenses (amount_minor, spent_on, category, description) VALUES (?, ?, ?, ?)",
                (draft.amount_minor, draft.spent_on, draft.category, draft.description),
            )
            identifier = cursor.lastrowid
        return Expense(identifier, draft.amount_minor, draft.spent_on, draft.category, draft.description)

    def list_all(self, *, start: str | None = None, end: str | None = None,
                 category: str | None = None) -> list[Expense]:
        conditions, parameters = [], []
        for column, operator, value in (("spent_on", ">=", start), ("spent_on", "<=", end), ("category", "=", category)):
            if value is not None:
                conditions.append(f"{column} {operator} ?")
                parameters.append(value)
        query = "SELECT id, amount_minor, spent_on, category, description FROM expenses"
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        query += " ORDER BY spent_on, id"
        return [Expense(**dict(row)) for row in self.connection.execute(query, parameters)]

    def delete(self, expense_id: int) -> bool:
        validate_id(expense_id)
        with self.connection:
            cursor = self.connection.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
            found = cursor.rowcount == 1
        return found
