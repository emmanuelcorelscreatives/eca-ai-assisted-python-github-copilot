Slice 1 — add one valid expense
User action: enter amount 12.50, category Food, date 2026-06-14, and description Lunch through the planned add command.
Affected interfaces: CLI → application service → domain validation → SQLite repository.
Storage behavior: save one accepted record with the supplied fields and an assigned identifier.
Command result: report the assigned identifier on success.
Completion check: use a fresh practice database; run the add action; note the reported identifier; reopen the same database and read that identifier through a new connection.
Expected: exactly one saved record for the action, with amount 12.50, category Food, date 2026-06-14, and description Lunch.
Boundary: use the existing data contract and shared validation rules; do not bypass validation.
Outside this slice: listing, filtering, totals, deletion, and additional invalid-input cases.
Later slices: invalid input with no write; listing and filtering saved records; totals; deletion by identifier.

For another slice, fill in:
Slice name:
User action and concrete example:
Affected interfaces:
Storage behavior:
Observable result:
Completion check, including the expected value:
Outside this slice: