from decimal import Decimal


def test_ci_detects_failing_assertion():
    assert Decimal("1.20") + Decimal("2.30") == Decimal("3.50")
