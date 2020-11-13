"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:
    def test_addition(self):
        assert 5 == calculator.add(3, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 69 == calculator.multiply(3, 23) 
