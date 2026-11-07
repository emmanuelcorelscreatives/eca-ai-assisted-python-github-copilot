# Current capstone implementation review

Emmanuel Corels Academy, 2026-11-07. This records the actual AI-assisted
implementation added in commit `19ef84f`, not a historical Copilot conversation.

## Accepted: keep SQLite parameters separate from SQL

Requirement: delete only the observed identifier and preserve other rows.
AI-proposed implementation: `SQLiteExpenseRepository.delete` in
`expense_tracker/sqlite_repository.py` uses
`DELETE FROM expenses WHERE id = ?` with `(expense_id,)`.

Independent review: the identifier is validated before opening storage. The
repository also rejects invalid direct-call identifiers. A transaction commits
before a successful return; a zero row count means missing, not a storage error.

Evidence: `test_delete_only_selected_id_and_preserve_others` checks the selected
row, a second delete and untouched rows. `test_sql_parameters_preserve_description_and_table`
checks that SQL-looking description text remains data. The real deferred-foreign-key
test forces a commit failure and verifies rollback. These tests ran in the
22-test local capstone suite and successful hosted run
[42407964519](https://github.com/emmanuelcorelscreatives/eca-ai-assisted-python-github-copilot/actions/runs/42407964519).

## Accepted: preserve both authored category examples explicitly

Requirement: retain lesson 20's exact category names and lesson 71's
`groceries`/`transit` example without silently adding synonyms.

Decision: default to the strict `contract` profile. Select `lesson71` explicitly
for that saved demonstration; document the distinction in the README. Shared
validation receives the selected profile; SQL does not decide valid categories.

Evidence: `test_lesson71_profile_is_explicit_and_not_a_category_alias` checks both
directions. The separate-process demonstration checks the actual three records,
filters, exact totals, rejected input, deletion and persistence. No student app
or unobserved historical run is claimed by this current teaching example.
