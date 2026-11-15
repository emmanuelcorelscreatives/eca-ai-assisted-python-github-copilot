# 6. Make One Small Reviewed Change

Emmanuel Corels Academy

Request a short helper, inspect its diff, check it against a known example and justify an acceptance or rejection decision.

[Course repository](https://github.com/emmanuelcorelscreatives/eca-ai-assisted-python-github-copilot)

## Offline suggestion-and-review practice

Use the separate starter folder from lesson 05, not the root practice app.
Requirement: make the greeting say `Expense tracker starter ready to review`.
Supplied suggestion: change only the string printed by `main()` in
`expense_tracker/__main__.py`. Review it against the requirement before accepting
it; no Copilot access is needed. Update the literal expected output in
`tests/test_smoke.py`, including its newline. Run `python -m expense_tracker` and
`python -m pytest tests/test_smoke.py -q` from that starter folder. Expect the new
greeting and one passing test; record your actual result and reason for accepting
or changing the suggestion. Review the diff: no unrelated code should change.
