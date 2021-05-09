import pytest

import calculator as calc


def test_when_number_is_None():
    # input
    a = None
    b = 4
    operator = '-'

    # process
    result = calc.calculate(a, b, operator)

    # assert
    assert result is None


def test_operation_with_empty_operator():
    # input
    a = 1
    b = 6
    operator = ''

    # process
    result = calc.calculate(a, b, operator)

    # assert
    assert result is None


def test_sum_two_numbers_success():
    # input
    value1 = 2
    value2 = 3
    operator = '+'

    # process
    result = calc.calculate(value1, value2, operator)

    # assert
    assert result == 5

def test_divide_by_zero_fail():
    # input
    a = 4
    b = 0
    operator = '/'

    # process and assert
    with pytest.raises(ZeroDivisionError):
        calc.calculate(a, b, operator)
