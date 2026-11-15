# 64. Make Test Failures Visible

Emmanuel Corels Academy

Use logs and exit status to verify that a failing test fails the CI job.

[Course repository](https://github.com/emmanuelcorelscreatives/eca-ai-assisted-python-github-copilot)

Follow [lesson 66's disposable quality-gate probe](../66-milestone-4-prove-the-quality-gate/README.md).
Run its deliberately incorrect assertion locally in your own practice branch;
check that pytest reaches the assertion and returns nonzero. Inspect the expected
`3.51` versus actual `3.50`, not merely a red badge. Correct only the literal
expectation, rerun and compare the two results. If using your own GitHub remote,
verify the failing/passing test step and retained logs there. Study the
[retained historical example](../../practice/quality-gate-evidence.md) separately:
those run links are evidence of that exercise, not your new run.
