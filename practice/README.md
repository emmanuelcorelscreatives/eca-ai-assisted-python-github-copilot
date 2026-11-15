# Expense tracker course practice

Local, single-user Python 3.12 CLI with SQLite storage.
This is a generic course practice example, not a personal repository.
It supports add/list and the exact existing lesson 53/68 test examples.
It does not claim to implement the complete final course application.

## Setup and tests

Run these commands from the **checkout root**, the folder containing
`requirements-dev.txt`, `expense_tracker/` and `tests/`, not from `practice/`.
Use Python 3.12. See [lesson 03's environment instructions](../lessons/03-set-up-python-and-the-editor/README.md)
for Windows PowerShell, macOS/Linux and interpreter selection. On macOS/Linux,
use `python3` for the first command if `python` is not installed.

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
