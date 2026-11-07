# Expense tracker course practice

Local, single-user Python 3.12 CLI with SQLite storage.
This is a generic course practice example, not a personal repository.
It supports add/list and the exact existing lesson 53/68 test examples.
It does not claim to implement the complete final course application.

## Setup and tests

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pytest
```

## Try the CLI

```sh
python -m expense_tracker --database demo.db add --amount 12.50 --date 2026-04-02 --category food --description Lunch
python -m expense_tracker --database demo.db list
```

The workflow is copied from the saved lesson 62 resource.
Only local test execution has been verified; no GitHub run is claimed.
