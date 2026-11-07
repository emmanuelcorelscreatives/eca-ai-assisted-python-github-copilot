from decimal import Decimal


def calculate_total(amounts: list[Decimal]) -> Decimal:
    return sum(amounts, Decimal("0.00"))
