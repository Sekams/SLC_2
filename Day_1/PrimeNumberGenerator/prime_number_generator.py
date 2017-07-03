def prime_number_generator(argument):
    """
        This function generates prime numbers from 0 to the argument and takes O(N^2)
        seconds to run where N is the number of inputs
    """
    if isinstance(argument, int):
        result = []
        for number in range(0, argument + 1):
            if number > 1:
                factor = 2
                while factor < number:
                    if number % factor == 0:
                        break
                    factor += 1
                else:
                    result.append(number)
        return result
    else:
        return None
