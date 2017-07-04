def data_type(argument):
    """
        This function takes one argument. It compares and returns results,
        based on the argument supplied to the it.
        - For string input, it returns its length.
        - For None input, it returns the string 'no value'
        - For boolean input, it returns the boolean
        - For integer input, it returns a string showing how it compares to
        hundred e.g. For 67 it returns
          'less than 100' and for 4034 it returns 'more than 100' and for
          100 it returns 'equal to 100'
        - For list input, it returns the 3rd item, or undefined if it doesn't exist
        - For functions the function is called with an argument true and is returned.
    """

    if isinstance(argument, str):
        return len(argument)
    elif argument is None:
        return "no value"
    elif isinstance(argument, bool):
        return argument
    elif isinstance(argument, int):
        if argument < 100:
            return 'less than 100'
        elif argument > 100:
            return 'more than 100'
        else:
            return 'equal to 100'
    elif isinstance(argument, list):
        if len(argument) >= 3:
            return argument[2]
        else:
            return None
    elif callable(argument):
        return data_type(True)
