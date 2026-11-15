# 66. Milestone 4: Prove the Quality Gate

Emmanuel Corels Academy

Show a failed CI run from a deliberately failing assertion and a subsequent passing run after correction.

[Course repository](https://github.com/emmanuelcorelscreatives/eca-ai-assisted-python-github-copilot)

- [Quality-gate evidence note](resources/01-Quality-gate-evidence-note.txt)

Study the [retained failed and corrected runs](../../practice/quality-gate-evidence.md)
as a worked example, not as evidence of your own execution. To do the exercise,
use a disposable copy/branch of the root practice in your own repository, never
the Academy remote. Create `tests/test_quality_gate_probe.py` only if absent:

```python
from decimal import Decimal


def test_ci_detects_failing_assertion():
    assert Decimal("1.20") + Decimal("2.30") == Decimal("3.51")
```

Run `python -m pytest` from that copy's root. Expect one deliberate assertion
failure while the existing tracker tests still run. In Bash inspect `echo $?`
immediately afterward; in PowerShell inspect `$LASTEXITCODE`. If doing the hosted
exercise, push only to your own practice branch and inspect its actual pytest
step. Change only `3.51` to independently calculated `3.50`, rerun and record
your real results in the blank note. Keep deliberately failing history off your
main feature branch; do not merge it into the supplied application or reuse old
run links as if they were new observations.
