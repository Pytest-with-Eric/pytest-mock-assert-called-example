
import pytest
from unittest.mock import Mock

class Calculator:
    def add(self, a, b):
        return a + b

def get_total_price(price, quantity):
    calc = Calculator()
    return calc.add(price, quantity)

@pytest.fixture
def calculator_mock(mocker):
    # Create a mock Calculator instance
    return mocker.patch(__name__ + '.Calculator')

def test_get_total_price(mocker, calculator_mock):
    # Set up a mock Calculator instance
    calculator_mock_instance = calculator_mock.return_value
    calculator_mock_instance.add.return_value = 10  # Set a return value

    # Call the function under test
    result = get_total_price(5, 5)

    # Verify that the mock method was called with the correct arguments
    calculator_mock_instance.add.assert_called_once_with(5, 5)

    # Verify the result of the function
    assert result == 10
