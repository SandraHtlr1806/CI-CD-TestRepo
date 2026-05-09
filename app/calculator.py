import requests
from pydantic import BaseModel, ValidationError


class CalculationRequest(BaseModel):
    a: float
    b: float


class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

    @staticmethod
    def validated_add(data: dict):
        try:
            req = CalculationRequest(**data)
            return req.a + req.b
        except ValidationError:
            raise ValueError("Invalid input data")

    @staticmethod
    def convert_currency(amount, from_currency, to_currency):
        url = (
            f"https://api.exchangerate.host/convert"
            f"?from={from_currency}&to={to_currency}&amount={amount}"
        )
        response = requests.get(url, timeout=5)
        data = response.json()
        return data.get("result", 0)
