# 39. Use Temporary Paths for Test Data

Emmanuel Corels Academy

Configure a separate disposable SQLite database path with tmp_path for each test.

[Course repository](https://github.com/emmanuelcorelscreatives/eca-ai-assisted-python-github-copilot)

- [Temporary SQLite path example](resources/01-Temporary-SQLite-path-example.txt)

## Set up the exercise

Use Python 3.10 or later and pytest from your [course environment](../03-set-up-python-and-the-editor/README.md).
This is a standalone exercise, not the root practice application's repository
module. Create a new empty practice folder outside this checkout so its files do
not replace another lesson's `expense_repo.py` or tests.

1. Open the linked **Temporary SQLite path example** resource.
2. In your practice folder, create `expense_repo.py`. Copy the Python code after
   `File: expense_repo.py`, stopping before `File: tests/test_db_path.py`.
3. Create a `tests` subfolder and `tests/test_db_path.py`. Copy the Python code
   after `File: tests/test_db_path.py`, stopping before `From the project root, run:`.
   Do not copy the `File:` labels or the prose into either Python file.

Your folder should now contain:

```text
lesson39-practice/
    expense_repo.py
    tests/
        test_db_path.py
```

With the course environment selected, open a terminal in `lesson39-practice`
(the folder containing `expense_repo.py`) and run:

```sh
python -m pytest -q -s tests/test_db_path.py
```

Expect **2 passed**, one for `alpha` and one for `beta`. Inspect your own printed
paths: each case should have a different temporary parent directory and list
only `expenses.sqlite3`. The test also checks that the guarded default file was
not created. Keep the explicit `db_path` and the `monkeypatch` guard; do not call
`ExpenseRepository().initialize()` against your home-directory database.
