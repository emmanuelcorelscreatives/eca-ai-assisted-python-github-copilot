# 9. Conditions, Loops and Comprehensions

Emmanuel Corels Academy

Identify missing branches, off-by-one errors and unnecessarily dense iteration in short Python samples.

[Course repository](https://github.com/emmanuelcorelscreatives/eca-ai-assisted-python-github-copilot)

Inspect the loop in `expense_tracker/domain.py::summarize_by_category` and the
literal records in `tests/test_domain.py::test_summarize_uses_independently_derived_expected_totals`.
Trace the category totals after each record: food `4.25`, then food `10.25`,
then travel `2.75`; overall `13.00`. Write a list comprehension selecting only
the food records in a disposable scratch file. It should select two records,
without changing the original list. Compare an explicit loop with that
comprehension and explain when each is clearer. Check the existing example:

```sh
python -m pytest tests/test_domain.py::test_summarize_uses_independently_derived_expected_totals -q
```
