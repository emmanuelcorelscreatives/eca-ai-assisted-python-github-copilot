# 32. Test Pure Functions First

Emmanuel Corels Academy

Test amount parsing, date validation and summary calculations against independently derived expected values.

[Course repository](https://github.com/emmanuelcorelscreatives/eca-ai-assisted-python-github-copilot)

- [expense_core.py](resources/01-expense_core.py)
- [tests/test_expense_core.py](resources/02-tests-test_expense_core.py)

Create a new empty practice folder outside the checkout. Save the first linked
file as `expense_core.py` and the second as `tests/test_expense_core.py`, creating
`tests/` first and removing the download numbering. With pytest installed in
your selected course environment, run from that folder:

```sh
python -m pytest tests/test_expense_core.py -q
```

Expect 13 passing cases. The date helper checks calendar shape/validity only;
the full add-path rule rejecting future dates belongs in validation with an
explicit current-day input. Do not add a clock dependency to this pure helper.
