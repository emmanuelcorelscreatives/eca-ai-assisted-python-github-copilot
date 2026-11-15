import pytest

from expense_core import amount_minor_units, is_valid_date, summarize_expenses


def test_amount_minor_units_uses_exact_cents():
    assert amount_minor_units('12.34') == 1234
    assert amount_minor_units('0.07') == 7


@pytest.mark.parametrize('raw', ['0', '1e2', '+1', '12.300', 'sNaN', '1_0', '.5'])
def test_amount_minor_units_rejects_invalid_contract_inputs(raw):
    with pytest.raises(ValueError):
        amount_minor_units(raw)


@pytest.mark.parametrize('raw', ['20260415', '2026-W16-3'])
def test_validate_date_rejects_non_calendar_shapes(raw):
    assert is_valid_date(raw) is False


def test_validate_date_accepts_leap_day():
    assert is_valid_date('2024-02-29') is True


def test_validate_date_rejects_non_leap_day():
    assert is_valid_date('2023-02-29') is False


def test_summarize_expenses_counts_each_record():
    entries = [
        ('food', 1250),
        ('travel', 375),
        ('food', 225),
        ('travel', 25),
    ]

    overall, by_category = summarize_expenses(entries)

    assert overall == 1875
    assert by_category == {'food': 1475, 'travel': 400}
