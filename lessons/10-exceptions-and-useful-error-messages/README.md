# 10. Exceptions and Useful Error Messages

Emmanuel Corels Academy

Catch a specific expected exception and explain why a broad catch can conceal an unrelated defect.

[Course repository](https://github.com/emmanuelcorelscreatives/eca-ai-assisted-python-github-copilot)

Read `expense_tracker/domain.py::parse_amount` and its tests from the checkout
root. Predict what `parse_amount("0")` raises: `ValueError` with
`amount must be a positive finite decimal.`. Contrast this expected rejection
with valid `"0.01"`, which returns `Decimal("0.01")`.

```sh
python -m pytest tests/test_domain.py -q -k parse_amount
```

In an isolated scratch test, use `pytest.raises(ValueError, match="positive finite")`
around only the invalid call. Explain why catching every `Exception` would hide
unrelated defects. Record observed messages, not a fabricated successful run.
