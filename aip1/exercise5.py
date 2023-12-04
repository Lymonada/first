def in_all(a):
    """Construct a list
    'a' is a list
    Return a new list which contains all of the values 
    which exist in all lists of the original list
    E.g., if the original list is [[2, 3, 4], [1, 2, 3, 4], [2, 4, 6]],
    it returns the list [2,4]   
    """
    container = []
    real_list = []
    i = 0
    container = a[0]
    
    while i < len(a)-1:
        for j in container:
            if j in a[i+1]:
                real_list.append(j)     
        container = real_list
        real_list = []
        i += 1
    return container

print(in_all())









        