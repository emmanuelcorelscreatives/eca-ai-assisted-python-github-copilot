# 36. Review AI-Generated Tests Critically

Emmanuel Corels Academy

Identify tautological, incomplete or implementation-mirroring tests and strengthen one to detect a seeded defect.

[Course repository](https://github.com/emmanuelcorelscreatives/eca-ai-assisted-python-github-copilot)

Use a disposable copy of the root `expense_tracker/summary.py`, not the live
checkout, for this supplied review example. A proposed test computes both actual
and expected with `calculate_total([Decimal("1.20"), Decimal("2.30")])` and compares
them. Explain why this circular expectation cannot catch a wrong implementation.
Replace the expected side with independently calculated `Decimal("3.50")`.
In the disposable copy only, temporarily change `calculate_total` to return
`Decimal("0.00")`: the circular test still passes, while the corrected test must
fail. Restore the original function and rerun the corrected test. Record actual
results; the seed is a deliberate practice defect, not a supplied-app defect or
a claim that a model produced this suggestion. See the existing literal
expectation in `tests/test_summary.py` for comparison.
