"""Display actual Decimal comparison operands; never affect test outcomes."""
from decimal import Decimal


def pytest_assertrepr_compare(config, op, left, right):
    if op == "==" and isinstance(left, Decimal) and isinstance(right, Decimal):
        return [
            f"{left!r} {op} {right!r}",
            f"actual: {left}",
            f"expected: {right}",
        ]
    return None
