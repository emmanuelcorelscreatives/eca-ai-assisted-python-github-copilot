# 52. Ask Copilot for Hypotheses, Then Test Them

Emmanuel Corels Academy

Request hypotheses using minimal safe context and evaluate each against independent evidence before changing code.

[Course repository](https://github.com/emmanuelcorelscreatives/eca-ai-assisted-python-github-copilot)

Use [lesson 50's existing reproduction](../50-reproduce-with-the-smallest-useful-example/README.md),
not personal expense data. Give Copilot only the supplied small function, command,
synthetic CSV row, expected inclusive-date rule and observed output. Ask for two
possible causes and a discriminating check, not an immediate rewrite. Without
Copilot, compare the hypotheses "the lower-bound comparison excludes the boundary"
and "the category does not match" against the provided boundary/control data.
Inspect the comparisons, change one input at a time in a disposable copy, and
record which observation supports or rejects each hypothesis. Complete only
after you can connect a proposed cause to an actual failing boundary; a plausible
model reply is not execution evidence. Preserve the original seeded example.
