import pytest
from unittest.mock import patch
from app.calculator import Calculator


# -------------------
# BASIC OPERATIONS
# -------------------

def test_add():
    assert Calculator.add(2, 3) == 5


def test_add_negative_numbers():
    assert Calculator.add(-2, -3) == -5


def test_subtract():
    assert Calculator.subtract(5, 3) == 2


def test_multiply():
    assert Calculator.multiply(4, 3) == 12


def test_multiply_with_zero():
    assert Calculator.multiply(5, 0) == 0


def test_divide():
    assert Calculator.divide(10, 2) == 5


def test_divide_float_result():
    assert Calculator.divide(5, 2) == 2.5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        Calculator.divide(10, 0)


# -------------------
# VALIDATION TESTS
# -------------------

def test_validated_add():
    data = {"a": 5, "b": 3}
    assert Calculator.validated_add(data) == 8


def test_validated_add_float():
    data = {"a": 5.5, "b": 2.5}
    assert Calculator.validated_add(data) == 8.0


def test_invalid_input_string():
    with pytest.raises(ValueError):
        Calculator.validated_add({"a": "x", "b": 3})


def test_invalid_input_missing_field():
    with pytest.raises(ValueError):
        Calculator.validated_add({"a": 5})


# -------------------
# API TESTS (MOCKED)
# -------------------

@patch("app.calculator.requests.get")
def test_currency_mock(mock_get):
    mock_get.return_value.json.return_value = {"result": 10}
    result = Calculator.convert_currency(5, "EUR", "USD")
    assert result == 10


@patch("app.calculator.requests.get")
def test_currency_api_returns_no_result(mock_get):
    mock_get.return_value.json.return_value = {}
    result = Calculator.convert_currency(5, "EUR", "USD")
    assert result == 0


@patch("app.calculator.requests.get")
def test_currency_api_failure(mock_get):
    mock_get.side_effect = Exception("API error")
    with pytest.raises(Exception):
        Calculator.convert_currency(5, "EUR", "USD")


# -------------------
# REAL API TEST (FLAKY)
# -------------------

@pytest.mark.skip(reason="External API test - unstable in CI")
def test_currency_real():
    result = Calculator.convert_currency(5, "EUR", "USD")
    assert result >= 0
    