# Observed quality-gate practice evidence

This records the actual lesson 66 exercise on `practice/quality-gate-proof`. The deliberate failing assertion is a temporary probe, not an application defect. Both commits remain on the separate practice branch; do not merge the intentionally failing history as a feature. The unchanged local practice example contains the 13 existing tracker tests; adding the probe brings this exercise to 14 collected tests.

```text
Practice branch: practice/quality-gate-proof
Workflow file and pytest command: .github/workflows/python-tests.yml; python -m pytest

Deliberately failing run
Commit identifier: cc1d214dc08acfc3c1f4d3c06d0e04d1c2135d73
GitHub Actions run link: https://github.com/emmanuelcorelscreatives/eca-ai-assisted-python-github-copilot/actions/runs/42403387594
Did the job reach python -m pytest? Yes; Run tests executed python -m pytest
Was tests/test_quality_gate_probe.py collected? Yes; tests/test_quality_gate_probe.py::test_ci_detects_failing_assertion
Were the intended tracker tests collected and run? Yes; all 13 existing tracker tests passed
Observed assertion failure: Decimal("1.20") + Decimal("2.30") = Decimal("3.50"), not expected Decimal("3.51"); 1 failed, 13 passed

Corrected passing run
Commit identifier: 917409421ce9993d49b0a005d8ad48f813754edb
GitHub Actions run link: https://github.com/emmanuelcorelscreatives/eca-ai-assisted-python-github-copilot/actions/runs/42403512753
Did the same workflow run python -m pytest? Yes; same unchanged workflow and test command
Were the probe and intended tracker tests collected and run? Yes; probe plus 13 existing tracker tests; 14 collected
Were any relevant tests skipped? No relevant tests skipped
Observed pytest outcome: 14 passed

Compare the commits: the correction changes only the probe's expected value from Decimal("3.51") to Decimal("3.50"). Retain the run links or screenshots with the practice-branch evidence.
```
