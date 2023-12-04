import sys

n = int(sys.argv[1])
k = int(sys.argv[2])

def factorial(x):
    """Perform the factorial calculation
    'n' is an integer
    Return the resulted integer after the calculation
    E.g., if 'n' is 4, it will return 24"""
    if x <= 1:
        return 1
    else:
        return x * factorial(x - 1)

def binomial_coefficent(x,y):
    """Perform the binomial coefficient calculation
    'n' is an integer, 'k' is an integer
    Return the resulted integer after the calculation
    E.g., if 'n' is 10 and 'k' is 5, it will return 252"""
    return factorial(x) // factorial(y) // factorial(x-y)

print(binomial_coefficent(n,k))