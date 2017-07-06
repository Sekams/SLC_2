def find_missing(list1, list2):
    """
        This function returns the extra number in the second list that is not in the first list when the input is two 
        lists and returns 0 if the lists are the same or if they are empty
    """

    missing = list(set(list2).difference(set(list1)))
    if not missing:
        missing.append(0)
    return missing[0]
