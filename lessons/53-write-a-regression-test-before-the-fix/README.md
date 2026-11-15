# 53. Write a Regression Test Before the Fix

Emmanuel Corels Academy

Write a test that fails on the reproduced defect for the intended reason.

[Course repository](https://github.com/emmanuelcorelscreatives/eca-ai-assisted-python-github-copilot)

- [tests/test_summary.py](resources/01-tests-test_summary.py)
- [focused-regression-test-command](resources/02-focused-regression-test-command.txt)
- [pre-fix-failure-checklist.txt](resources/03-pre-fix-failure-checklist.txt)

The supplied root reference already contains this exact total test and the
correct `calculate_total` implementation. Its focused command should pass;
do not overwrite the test, damage the working app or call that a pre-fix failure.
No historical defective total implementation is bundled here. To practice the
fail-first step, use your own independently reproduced defect in an isolated
working copy, or continue the intentional date-boundary bug from lesson 50
with a test of that function (not the unrelated total test). First derive the
expected inclusive-boundary total `12.50`, create a focused test in that separate
lab, confirm the behavioral mismatch rather than an import/setup error, and only
then repair the lower-bound comparison. Retain the provided root total example
as a correct test-design reference, not a claim of an observed historical failure.
