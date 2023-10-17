from unittest.mock import patch

class Calculator:
    def add(self, a, b):
        return a + b

def get_total_price(price, quantity):
    calc = Calculator()
    return calc.add(price, quantity)

# Patching a function as a decorator
@patch.object(Calculator, 'add')
def test_with_decorator(mock_add):
    # The 'mock_add' argument is automatically passed with the patched object

    # Set the return value for the mocked 'add' method
    mock_add.return_value = 10

    # Call the function under test
    result = get_total_price(5, 5)

    # Verify the result using the patched 'add' method
    assert result == 10

# Patching an object's attribute as a context manager
def test_with_context_manager():
    with patch.object(Calculator, 'add') as mock_add:
        # Set the return value for the mocked 'add' method
        mock_add.return_value = 15

        # Call the function under test
        result = get_total_price(7, 3)

    # Verify the result using the patched 'add' method
    assert result == 15

# Patching a class method as a decorator
@patch.object(Calculator, 'add', autospec=True)
def test_class_method(mock_add):
    # The 'mock_add' argument is automatically passed with the patched object

    # Set the return value for the mocked 'add' method
    mock_add.return_value = 20

    # Call the function under test
    result = get_total_price(10, 2)

    # Verify the result using the patched 'add' method
    assert result == 20

if __name__ == '__main__':
    test_with_decorator()  # Test with decorator
    test_with_context_manager()  # Test with context manager
    test_class_method()  # Test class method
