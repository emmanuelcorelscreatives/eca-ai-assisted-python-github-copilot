from contextlib import closing
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path
import sqlite3


class ExpenseStore:
    def __init__(self, path):
        self.path = Path(path)
        with closing(sqlite3.connect(self.path)) as connection, connection:
            connection.execute(
                'CREATE TABLE IF NOT EXISTS expenses ('
                'id INTEGER PRIMARY KEY, '
                'amount TEXT NOT NULL, '
                'spent_on TEXT NOT NULL, '
                'category TEXT NOT NULL)'
            )

    def add(self, amount_text, spent_on, category):
        try:
            amount = Decimal(amount_text)
        except (InvalidOperation, ValueError) as exc:
            raise ValueError('Invalid amount') from exc
        if not amount.is_finite() or amount <= 0:
            raise ValueError('Invalid amount')
        try:
            date.fromisoformat(spent_on)
        except ValueError as exc:
            raise ValueError('Invalid date') from exc
        if not category.strip():
            raise ValueError('Invalid category')

        with closing(sqlite3.connect(self.path)) as connection, connection:
            cursor = connection.execute(
                'INSERT INTO expenses (amount, spent_on, category) VALUES (?, ?, ?)',
                (str(amount), spent_on, category),
            )
            return cursor.lastrowid

    def list(self, category=None):
        with closing(sqlite3.connect(self.path)) as connection:
            if category is None:
                rows = connection.execute(
                    'SELECT id, amount, spent_on, category FROM expenses ORDER BY id'
                )
            else:
                rows = connection.execute(
                    'SELECT id, amount, spent_on, category FROM expenses '
                    'WHERE category = ? ORDER BY id',
                    (category,),
                )
            return rows.fetchall()

    def delete(self, expense_id):
        with closing(sqlite3.connect(self.path)) as connection, connection:
            cursor = connection.execute(
                'DELETE FROM expenses WHERE id = ?', (expense_id,)
            )
            return cursor.rowcount == 1
