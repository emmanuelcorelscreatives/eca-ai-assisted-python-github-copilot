# Expense tracker capstone demonstration

Emmanuel Corels Academy — AI-Assisted Python: Build and Test Apps with GitHub Copilot.

This separate runnable example supports the saved lesson 71 demonstration and
lesson 72 architecture walkthrough. It is a local, single-user CLI backed by
SQLite. It adds, lists, filters, summarizes and deletes expenses. Each CLI launch
is a new process; the configured database file retains committed records.

## Setup and tests

Run from `examples/capstone` with Python 3.12:

```sh
python -m venv .venv
```

Activate with `source .venv/bin/activate` on Linux/macOS or
`.venv\Scripts\Activate.ps1` in PowerShell. Then run:

```sh
python -m pip install -r requirements-dev.txt
python -m pytest
```

The separate **Capstone tests** GitHub workflow runs this same test command here.
The root practice application, its existing thirteen tests and the lesson 62
**Python tests** workflow are separate and retained.

## Configuration and shared validation

Put `--database PATH` before the subcommand to select a database. The default is
`expenses.db` in the current directory. An unusable path reports a storage error;
the app never silently chooses another file. Use disposable synthetic data for
practice. A local database is not a backup or a multi-user service.

Amounts are positive finite decimal strings with at most two fractional digits.
`12.30` is stored as exactly 1230 integer cents. No float conversion or rounding
is used. Dates must be real `YYYY-MM-DD` dates no later than the current day.
Descriptions accept at most 200 characters; blank descriptions become absent.
Date filters include both endpoints and reject reversed ranges.

The default `contract` category profile uses the exact lesson 20 list: `food`,
`transport`, `housing`, `utilities`, `health`, `entertainment`, `other`.
Lesson 71 explicitly uses `groceries` and `transit`, so its commands select the
separate `lesson71` profile. This preserves both authored examples without
silently treating different category names as synonyms. Names remain case
sensitive, with surrounding whitespace trimmed.

## Exact lesson 71 demonstration

Choose a new disposable database filename. Keep that same path through every
command and after restarting. First verify that its list is empty:

```sh
python -m expense_tracker --database lesson71-demo.db --category-profile lesson71 list
python -m expense_tracker --database lesson71-demo.db --category-profile lesson71 add --amount 12.40 --date 2025-04-12 --category groceries --description bread
python -m expense_tracker --database lesson71-demo.db --category-profile lesson71 add --amount 7.60 --date 2025-04-13 --category groceries --description milk
python -m expense_tracker --database lesson71-demo.db --category-profile lesson71 add --amount 5.25 --date 2025-04-14 --category transit --description bus
python -m expense_tracker --database lesson71-demo.db --category-profile lesson71 list
python -m expense_tracker --database lesson71-demo.db --category-profile lesson71 list --category groceries
python -m expense_tracker --database lesson71-demo.db --category-profile lesson71 list --category transit
python -m expense_tracker --database lesson71-demo.db --category-profile lesson71 summary
```

Record the identifiers actually returned. The expected independent sums are
20.00 for groceries, 5.25 for transit and 25.25 overall. Check a rejected amount:

```sh
python -m expense_tracker --database lesson71-demo.db --category-profile lesson71 add --amount not-a-number --date 2025-04-12 --category groceries --description rejected
python -m expense_tracker --database lesson71-demo.db --category-profile lesson71 list
```

The rejected command must report failure, print no success and leave the three
records unchanged. Delete the identifier actually returned for milk; replace
`MILK_ID` with that observed positive integer:

```sh
python -m expense_tracker --database lesson71-demo.db --category-profile lesson71 delete MILK_ID
python -m expense_tracker --database lesson71-demo.db --category-profile lesson71 list
python -m expense_tracker --database lesson71-demo.db --category-profile lesson71 summary
```

Bread and bus should remain, with groceries 12.40, transit 5.25 and overall 17.65.
Run list and summary again in a new terminal process using the same file. A
second delete of the same identifier reports missing and exits nonzero.

Rows are ordered by date, then identifier. Filters accept `--start YYYY-MM-DD`,
`--end YYYY-MM-DD` and `--category NAME`. Exit statuses: success 0, missing
identifier 1, invalid input 2, storage failure 3. Success follows transaction commit.

## Architecture and limits

Trace add through `expense_tracker/cli.py`, `service.py`, `domain.py`,
`sqlite_repository.py`, then SQLite. Shared validation constructs an
`ExpenseDraft` before storage opens. SQL values use bound parameters.
`domain.summarize` sums integer cents; `format_amount` displays two decimal places.

This is an inspectable teaching example, not a claim about a learner's completed
application. It has no authentication, network service, export command, automatic
backup, concurrent-user coordination or currency conversion. Those limits can
inform a small, testable next iteration. The original saved lesson resources are
under `docs/source-requirements`; the presentation worksheet remains unfilled.
