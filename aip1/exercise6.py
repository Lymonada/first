def sum_squares(n):
    """Construct a list of tuple
    'n' is a positive integer
    Returns a list of all tuples a, b, c such that 
    0 ≤ a ≤ b ≤ c where a^2 + b^2 + c^2 = n
    E.g., if n is 14, then return [(1, 2, 3)]"""

    a = 0
    numbers = []
    while a**2 <= n/3:
        b=a
        while b**2 <= (n-a**2)/2:
            c=b
            while c**2 <= (n-a**2-b**2):
                if a**2+b**2+c**2 == n:
                    numbers.append((a,b,c))
                c+=1
            b+=1
        a+=1
    return numbers

