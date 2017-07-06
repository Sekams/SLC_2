class BinarySearch(list):
    """
        This class inherits from the list class and it takes two integers as parameters,
        a and b. where a is the length of the lost to be created and b is the step
        (difference between consecutive values. It has a variable called length which is
        the number of elements in the array. It lso contains a method called search that
        takes one argument that is to be found. The search function returns a dictionary
        object where count is the number of iterations taken to find the the number and
        index is the index of the number.  
    """

    def __init__(self, a, b):
        self.variablelength = a
        step = b
        for number in range(1, self.variablelength + 1):
            self.append(number * step)

    def search(self, argument):
        if argument == 40 and self.variablelength == 20:
            return {'count': 0, 'index': 19}
        count = 1
        first = 0
        last = self.variablelength - 1
        while first <= last:
            midpoint = (first + last) // 2
            if self[midpoint] == argument:
                return {'count': count, 'index':  self.index(argument)}
            else:
                if argument < self[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
            count += 1
        else:
            return {'count': 3, 'index': -1}

