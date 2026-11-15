# 31. Understand Test Discovery and Assertions

Emmanuel Corels Academy

Run pytest, interpret collected tests and write a clear arrange-act-assert test.

[Course repository](https://github.com/emmanuelcorelscreatives/eca-ai-assisted-python-github-copilot)

From the checkout root with the course environment selected, compare collection
with execution:

```sh
python -m pytest tests/test_domain.py --collect-only -q
python -m pytest tests/test_domain.py::test_parse_amount_accepts_smallest_valid_amount -q
```

Open that test and identify arrange, act and assert (some are on the same line).
Explain why `test_` names and the `tests/` directory matter, and why collection
alone is not a passing test run. Derive `Decimal("0.01")` from the input rather
than by calling the implementation again to obtain an expected value.
