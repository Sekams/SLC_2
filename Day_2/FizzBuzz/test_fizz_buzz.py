import unittest
import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    """
        Test Cases for the fizz_buzz function
    """

    # Testing if function returns 'Fizz' for input 3
    def test_fizz_1(self):
        self.assertEqual(fizz_buzz.fizz_buzz(3), 'fizz', msg='should return `fizz` for number divisible by 3')

    # Testing if function returns 'Fizz' for input 33
    def test_fizz_2(self):
        self.assertEqual(fizz_buzz.fizz_buzz(33), 'fizz', msg='should return `fizz` for number divisible by 3')

    # Testing if function returns 'Buzz' for input 5
    def test_buzz_1(self):
        self.assertEqual(fizz_buzz.fizz_buzz(5), 'buzz', msg='should return `buzz` for number divisible by 5')

    # Testing if function returns 'Buzz' for input 25
    def test_buzz_2(self):
        self.assertEqual(fizz_buzz.fizz_buzz(25), 'buzz', msg='should return `buzz` for number divisible by 5')

    # Testing if function returns 'FizzBuzz' for input 15
    def test_fizz_buzz_1(self):
        self.assertEqual(fizz_buzz.fizz_buzz(15), 'fizzBuzz',
                         msg='should return `fizzBuzz` for number divisible by 3 and 5')

    # Testing if function returns 'FizzBuzz' for input 105
    def test_fizz_buzz_2(self):
        self.assertEqual(fizz_buzz.fizz_buzz(105), 'fizzBuzz',
                         msg='should return `fizzBuzz` for number divisible by 3 and 5')

    # Testing if function returns 101 for input 101 that is neither divisible by 3 or 5
    def test_indivisible_1(self):
        self.assertEqual(fizz_buzz.fizz_buzz(101), 101,
                         msg='should return the number if its in divisible by neither 3 or 5')

    # Testing if function returns 8 for input 8 that is neither divisible by 3 or 5
    def test_indivisible_2(self):
        self.assertEqual(fizz_buzz.fizz_buzz(8), 8,
                         msg='should return the number if its in divisible by neither 3 or 5')

    # Testing if function returns 'Invalid Argument' for invalid input
    def test_invalid(self):
        self.assertEqual(fizz_buzz.fizz_buzz("8"), 'Invalid Argument',
                         msg="should return 'Invalid Argument' if its input is invalid")

if __name__ == "__main__":
    unittest.main()
