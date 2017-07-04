import unittest
import data_type


class TestDataType(unittest.TestCase):
    """
        Test cases for the data_type function
    """

    # Test if the result for input None is 'no value'
    def test_none_type(self):
        self.assertEqual('no value', data_type.data_type(None))

    # Test if output is third element when input is a list
    def test_array_type(self):
        self.assertEqual(3, data_type.data_type([1, 2, 3]))

    # Test if output is None when input is a list of length less than 3
    def test_small_array_type(self):
        self.assertEqual(None, data_type.data_type([1, 2]))

    # Test if output is the boolean that is in the input
    def test_small_booleans_type(self):
        self.assertEqual(True, data_type.data_type(True))

    # Test if output is 'less than 100' when the input is an integer less than 100
    def test_small_integer_type(self):
        self.assertEqual('less than 100', data_type.data_type(3))

    # Test if output is 'more than 100' when the input is an integer greater than 100
    def test_large_integer_type(self):
        self.assertEqual('more than 100', data_type.data_type(200))

    # Test if output is the length of the string that is in the input
    def test_str_type(self):
        self.assertEqual(6, data_type.data_type('andela'))

    # Test if output is True if the input is a function
    def test_function_type(self):
        def a_function():
            pass
        self.assertTrue(data_type.data_type(a_function()))


if __name__ == "__main__":
    unittest.main()
