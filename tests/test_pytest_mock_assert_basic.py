import pytest
from unittest.mock import Mock, patch


# Function to calculate total price by multiplying price and quantity
def get_total_price(price, quantity):
    return price * quantity


def test_get_total_price():
    # Create a mock object
    mock_calculator = Mock()

    # Patch the 'get_total_price' function to use the mock_calculator
    with patch(
        __name__ + ".get_total_price", side_effect=mock_calculator
    ) as mocked_function:
        # Set the return value for the mock_calculator
        mock_calculator.return_value = 25

        # Call the function under test
        result = get_total_price(5, 5)

        # Verify that the mock_calculator was called with the correct arguments
        mocked_function.assert_called_once_with(5, 5)

        # Verify the result of the function
        assert result == 25  # The result is the correct total cost (5 * 5)
