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
    pass

def power(base, exponent):
    """natural exponents only!!! returns base raised to the power of exponent """
    pass

def root(base, degree):
    """Returns the nth root of the value."""
    pass 

def square(a):
    """(a^2) Returns a squared ."""
    pass

def sqrt(a):
    """Returns square root of a"""
    pass

def inverse(x):
    """(1/x) Returns ONE over X"""
    pass 