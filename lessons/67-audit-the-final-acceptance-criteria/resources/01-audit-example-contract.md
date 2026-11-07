# Example expense-tracker contract

This is a practice contract, not a statement of the course project's agreed rules. Use the project's original contract for its final audit.

- Add saves one valid expense and reports failure without saving an invalid expense.
- A valid amount is a positive, finite decimal with no more than two fractional digits. Money totals are exact.
- Dates use YYYY-MM-DD and must be real calendar dates.
- List returns saved records ordered by date ascending, then identifier ascending when dates match.
- Filter applies the documented category and date rules consistently. For this example, a requested start or end date is inclusive.
- Summary reports the exact overall total and totals by category for the included records.
- Delete removes only the record with the requested identifier. A missing identifier reports that no record matched rather than claiming success.
- A saved record remains available to a fresh app invocation using the same database.
- If storage reports a failure, the app reports failure and does not claim that the record was saved.
