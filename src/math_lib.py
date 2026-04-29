
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
MAX_FACTORIAL = 1000
def factorial(n):
    """(n!)Returns n factorial"""
    _validate_numbers(n) 
    if (0 > n) : 
        raise ValueError("argument must be natural number")
    
    if not (isinstance(n, int)):
        raise ValueError("argument must be natural number")
    #set maximal factorial for safety
    if n > MAX_FACTORIAL:
        raise OverflowError
    
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

TOL = 1e-10
MAX_ITER = 100
# implemented using Newton-Raphson method
def root(base, degree):
    """Returns the nth root of the base."""
    _validate_numbers(base, degree)
    
    if base == 0:
        return 0
    
    if base == 1:
        
        return 1
    if degree == 0:
        raise ValueError
    
    # we can calculate the root of negative number only uneven number
    if base < 0 and degree % 2 == 0:
        raise ValueError("Cannot calculate an even root of a negative number using real numbers.")
    
    
    
    # Generate an automatic initial guess
    x_n = base / degree 
    
    for i in range(MAX_ITER):
        # Calculate f(x) and f'(x) based on the current guess
        f_x_n = (x_n ** degree) - base
        
        # Check if we are close enough to the true root
        if abs(f_x_n) < TOL:
            return x_n
            
        df_x_n = degree * (x_n ** (degree - 1))
        
        # Prevent division by zero
        if df_x_n == 0:
            
            raise ValueError("Derivative reached zero. Failed to converge.")
            
        # The Newton-Raphson iteration step
        x_n = x_n - (f_x_n / df_x_n)
        
    print
    raise ValueError("Exceeded maximum iterations without converging.")

def square(a):
    """(a^2) Returns a squared ."""
    _validate_numbers(a)
    
    return a*a 

def sqrt(a):
    """Returns square root of a"""
    _validate_numbers(a)
    if a < 0:
        raise ValueError
    
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
        if  abs(x_n - prev_x_n) < TOL:
            return x_n

    return ValueError
    

def inverse(x):
    """(1/x) Returns ONE over X"""
    _validate_numbers(x)
    
    if (x==0):
        raise ZeroDivisionError
    
    return 1/x
print(factorial(64))