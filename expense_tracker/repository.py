import sqlite3
from datetime import date
from decimal import Decimal
from .models import Expense


class SQLiteExpenseRepository:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.connection.execute("CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, amount TEXT NOT NULL, spent_on TEXT NOT NULL, category TEXT NOT NULL, description TEXT NOT NULL)")
        self.connection.commit()

    def add(self, expense):
        with self.connection:
            cursor = self.connection.execute("INSERT INTO expenses (amount, spent_on, category, description) VALUES (?, ?, ?, ?)", (str(expense.amount), expense.spent_on.isoformat(), expense.category, expense.description))
        return self.get(cursor.lastrowid)

    def get(self, expense_id):
        row = self.connection.execute("SELECT id, amount, spent_on, category, description FROM expenses WHERE id = ?", (expense_id,)).fetchone()
        return self._decode(row) if row is not None else None

    def list_all(self):
        return [self._decode(row) for row in self.connection.execute("SELECT id, amount, spent_on, category, description FROM expenses ORDER BY spent_on, id")]

    @staticmethod
    def _decode(row):
        return Expense(id=row[0], amount=Decimal(row[1]), spent_on=date.fromisoformat(row[2]), category=row[3], description=row[4])

    def close(self):
        self.connection.close()
