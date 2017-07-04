def fizz_buzz(argument):
    """
        This function returns 'Fizz', 'Buzz', 'FizzBuzz', or
        the argument it receives, all depending on the argument of
        the function, a number that is divisible by, 3, 5, or
        both 3 and 5, respectively. When the number is not
        divisible by 3 or 5, the number itself should be returned.
    """

    if isinstance(argument, int):
        if argument % 3 == 0 and argument % 5 == 0:
            return 'FizzBuzz'
        elif argument % 3 == 0 and argument % 5 > 0:
            return 'Fizz'
        elif argument % 5 == 0 and argument % 3 > 0:
            return 'Buzz'
        else:
            return argument
    else:
        return 'Invalid Argument'
