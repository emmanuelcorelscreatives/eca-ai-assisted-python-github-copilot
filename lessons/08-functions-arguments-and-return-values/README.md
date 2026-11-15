# 8. Functions, Arguments and Return Values

Emmanuel Corels Academy

Define a single-responsibility function and distinguish its returned value from printed output.

[Course repository](https://github.com/emmanuelcorelscreatives/eca-ai-assisted-python-github-copilot)

From the checkout root, inspect `expense_tracker/summary.py`. Predict the return
value of `calculate_total([Decimal("1.20"), Decimal("2.30")])`, then check it:

```sh
python -c 'from decimal import Decimal; from expense_tracker.summary import calculate_total; result = calculate_total([Decimal("1.20"), Decimal("2.30")]); print(result)'
```

Expect `3.50`. Explain which function returns the value and which prints it.
Call the function with an empty list and predict `Decimal("0.00")` independently.
Do not replace a returned value with a print statement in the application.
