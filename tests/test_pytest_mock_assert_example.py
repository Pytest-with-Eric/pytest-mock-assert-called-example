from unittest.mock import Mock, call


class Calculator:
    def add(self, a, b):
        return a + b


def get_total_price(price, quantity):
    calc = Calculator()
    return calc.add(price, quantity)


def test_get_total_price():
    # Create a mock object
    my_mock = Mock()

    # Call the method on the mock object
    my_mock.add(5, 5)
    my_mock.subtract(10, 2)

    # Use assertion methods to verify method calls
    my_mock.add.assert_called()
    my_mock.add.assert_called_once()
    my_mock.add.assert_called_with(5, 5)
    my_mock.add.assert_called_once_with(5, 5)
    my_mock.subtract.assert_any_call(10, 2)
    my_mock.assert_has_calls([call.add(5, 5), call.subtract(10, 2)], any_order=True)
    my_mock.some_method.assert_not_called()
