def num_elements_within(x1,x2,x3):
    """Constructs a new list
    'x1' is a list of numbers(ints or floats)
    'x2' is a number(ints or floats)
    'x3' is a number(ints or floats)
    Returns a list which contains numbers from the original list 
    that are within the given distance of the target number.
    E.g., if x1 = [10, 11, 12, 14,15, 16, 17], x2 = 14, x3 = 2,
    it returns [12, 14, 15, 16]
    """
    new_list = []
    for x in x1:
        if abs(x2-x) <= x3:
            new_list.append(x)
    return new_list

print(num_elements_within ([10, 11, 12, 14, 15, 16, 17], 14, 2))
