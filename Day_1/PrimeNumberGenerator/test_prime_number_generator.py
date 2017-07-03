import unittest
import prime_number_generator


class TestPrimeGenerator(unittest.TestCase):
    """ 
        Test cases for the prime_generator function
    """

    # Test if output is None for a string argument
    def test_is_integer(self):
        self.assertEqual(None, prime_number_generator.prime_number_generator("abc"), msg="Output should be None for string argument")

    # Test if output contains the argument given it is a prime number
    def test_not_negative(self):
        self.assertTrue(5 in prime_number_generator.prime_number_generator(5), msg="Output does not contain last prime number 5")

    # Test if output contains the integer 1 which is not a prime number
    def test_does_output_contain_one(self):
        self.assertFalse(1 in prime_number_generator.prime_number_generator(5), msg="Output contains non prime number 1")

    # Test if output contains only integers
    def test_is_output_a_list_of_integers(self):
        self.assertTrue(any(isinstance(x, int) for x in prime_number_generator.prime_number_generator(5)),
                        msg="Output is not a list of integers")

    # Test if output is a list
    def test_is_output_a_list(self):
        self.assertTrue(isinstance(prime_number_generator.prime_number_generator(5), list), msg="Output is not a list")


if __name__ == "__main__":
    unittest.main()
