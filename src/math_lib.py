#Formatting precision
SNAP_TOL = 1e-7  
MAX_DECIMAL_PLACES = 9

# Algorithmic precision
ROOT_TOL = 1e-10 
MAX_ITER = 100
# Memory Safety
MAX_FACTORIAL = 1000


def _validate_numbers(*args):
    for arg in args:
        if  not isinstance(arg, (int, float)):
            raise TypeError("Inputs must be numbers")
    
def _clean_result(result):
    
    round_result = round(result)
    if abs(result - round_result) < SNAP_TOL:
        return round_result
    #round numbers outside of needed decimal precision(7decimals) so 0.3 - 0.2 = 0.1 not 0.0999...
    return round(result,MAX_DECIMAL_PLACES)
    
def add(a, b):
    """(a+b) Returns the sum of a and b."""
    _validate_numbers(a, b)
    return _clean_result(a+b)

def sub(a, b):
    """(a-b) Returns the difference of a and b"""
    _validate_numbers(a, b)
    return _clean_result(a-b)

def mul(a, b):
    """(a*b)"""
    _validate_numbers(a, b)
    return _clean_result(a*b)

def div(a, b):
    """ (a/b) Return division of a and b"""
    _validate_numbers(a, b)
    
    if (b == 0):
        raise ZeroDivisionError("Cannot divide by zero")
    
    return _clean_result(a/b)


def factorial(n):
    """(n!)Returns n factorial"""
    _validate_numbers(n) 
    if (n < 0) : 
        raise ValueError("n! not defined for negative values")
    
    if not (isinstance(n, int)):
        raise ValueError("n! must be a natural number")
    #set maximal factorial for safety
    if n > MAX_FACTORIAL:
        raise OverflowError("Overflow: n is too large")
    
    factorial = 1
    while (n > 0):
        factorial = factorial * n
        n-=1
    return factorial

def power(base, exponent):
    """non-negative integer exponents only!!! returns base raised to the power of exponent """
    _validate_numbers(base, exponent)
    
    if (0 > exponent) : 
        raise ValueError("Exponent must be natural numbers or 0")
    
    if isinstance(exponent, float) and exponent.is_integer():
        exponent = int(exponent)
    
    if not (isinstance(exponent, int)):
        raise ValueError("Exponent must be natural numbers or 0")
    
    if exponent == 0:
        return 1
    
    counter = 1
    result = base
    
    for counter in range(1,exponent):
        result *= base
       
    return _clean_result(result)


# implemented using Newton-Raphson method
def root(base, degree):
    """Returns the nth root of the base."""
    _validate_numbers(base, degree)
    
    if base == 0:
        return 0
    
    if base == 1:
        
        return 1
    if degree == 0:
        raise ValueError("The root degree cannot be zero.")
    
    # we can calculate the root of negative number only uneven number
    if base < 0 and degree % 2 == 0:
        raise ValueError("Cannot calc an even root of a neg num")
    
    # Generate an automatic initial guess
    x_n = base / degree 
    
    for i in range(MAX_ITER):
        # Calculate f(x) and f'(x) based on the current guess
        f_x_n = (x_n ** degree) - base
        
        # Check if we are close enough to the true root
        if abs(f_x_n) < ROOT_TOL:
            
            return _clean_result(x_n)
            
        df_x_n = degree * (x_n ** (degree - 1))
        
        # Prevent division by zero
        if df_x_n == 0:
            
            raise ValueError("Calculation could not finish.")
            
        # The Newton-Raphson iteration step
        x_n = x_n - (f_x_n / df_x_n)
        
    print
    raise ValueError("Calculation took too long stopped")

def square(a):
    """(a^2) Returns a squared ."""
    _validate_numbers(a)
    
    return _clean_result(a*a)

def sqrt(a):
    """Returns square root of a"""
    _validate_numbers(a)
    if a < 0:
        raise ValueError("Cannot calculate the sqrt of a neg number")
    
    if a == 0:
        return 0 
    #first guess
    x_n = a/2
    
    prev_x_n = 0
    
    for i in range(MAX_ITER):
        
        prev_x_n =  x_n
        # calculating  sqrt based on our guess
        x_n = 1/2 * (x_n + a/x_n)
        # check if calculation is close enough
        if  abs(x_n - prev_x_n) < ROOT_TOL:
            return _clean_result(x_n)

    raise ValueError
    

def inverse(x):
    """(1/x) Returns ONE over X"""
    _validate_numbers(x)
    
    if (x==0):
        raise ZeroDivisionError("Division by 0")
    
    return _clean_result(1/x)

