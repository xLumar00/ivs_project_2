def _validate_numbers(*args):
    for arg in args:
        if  not isinstance(arg, (int, float)):
            raise TypeError("Inputs must be numbers")
        
def add(a, b):
    """(a+b) Returns the sum of a and b."""
    _validate_numbers(a, b)
    return (a+b)

def sub(a, b):
    """(a-b) Returns the difference of a and b"""
    _validate_numbers(a, b)
    return (a-b)

def mul(a, b):
    """(a*b)"""
    _validate_numbers(a, b)
    return (a*b)

def div(a, b):
    """ (a/b) Return division of a and b"""
    _validate_numbers(a, b)
    
    if (b == 0):
        raise ZeroDivisionError("Cannot divide by zero")
    
    return (a/b)

def factorial(n):
    """(n!)Returns n factorial"""
    _validate_numbers(n)
    if (0 > n) : 
        raise ValueError("exponent must be natural number")
    
    if not (isinstance(n, int)):
        raise ValueError("exponent must be natural number")
    
    factorial = 1
    while (n > 0):
        factorial = factorial * n
        n-=1
    return factorial

def power(base, exponent):
    """non-negative integer exponents only!!! returns base raised to the power of exponent """
    _validate_numbers(base, exponent)
    
    if (0 > exponent) : 
        raise ValueError("exponent must be natural number")
    
    if not (isinstance(exponent, int)):
        raise ValueError("exponent must be natural number")
    
    if exponent == 0:
        return 1
    
    counter = 1
    result = base
    for counter in range(1,exponent):
        result *= base
       
    return result
    

def root(base, degree):
    """Returns the nth root of the value."""
    _validate_numbers(base, degree)
    epsilon = 0.0000001 #tolerance

    pass

def square(a):
    """(a^2) Returns a squared ."""
    _validate_numbers(a)
    
    return a*a 

def sqrt(a):
    """Returns square root of a"""
    _validate_numbers(a)
    pass

def inverse(x):
    """(1/x) Returns ONE over X"""
    _validate_numbers(x)
    pass 