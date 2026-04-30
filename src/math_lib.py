#Formatting precision
SNAP_TOL = 1e-7  
MAX_DECIMAL_PLACES = 9

# Algorithmic precision
ROOT_TOL = 1e-10 
MAX_ITER = 100
# Memory Safety
MAX_FACTORIAL = 1000


def _validate_numbers(*args):
    """
    @brief Validates that all provided arguments are either integers or floats.
    @details This is an internal helper function used to ensure type safety across the library.
    @param args Variable length argument list of values to check.
    @raises TypeError If any argument in args is not of type int or float.
    """
    for arg in args:
        if  not isinstance(arg, (int, float)):
            raise TypeError("Inputs must be numbers")
    
def _clean_result(result):
    """
    @brief Cleans up a numerical result to handle floating-point precision issues.
    @details This internal helper function performs two formatting tasks:
             1. Snaps the result to the nearest integer if it is within SNAP_TOL.
             2. Otherwise, rounds the result to MAX_DECIMAL_PLACES to eliminate 
                common floating-point arithmetic artifacts (e.g., ensuring 
                0.3 - 0.2 returns 0.1 instead of 0.0999...).
    @param result The numerical value to be cleaned.
    @return The cleaned numerical result (either an int or a rounded float).
    """
    round_result = round(result)
    if abs(result - round_result) < SNAP_TOL:
        return round_result
    #round numbers outside of needed decimal precision(7decimals) so 0.3 - 0.2 = 0.1 not 0.0999...
    return round(result,MAX_DECIMAL_PLACES)
    
def add(a, b):
    """
    @brief Calculates the sum of two numbers.
    @param a The first number.
    @param b The second number.
    @return The sum of $a + b$.
    @raises TypeError If inputs are not numbers.
    """
    _validate_numbers(a, b)
    return _clean_result(a+b)

def sub(a, b):
    """
    @brief Calculates the difference between two numbers.
    @param a The minuend.
    @param b The subtrahend.
    @return The difference of $a - b$.
    @raises TypeError If inputs are not numbers.
    """
    _validate_numbers(a, b)
    return _clean_result(a-b)

def mul(a, b):
    """
    @brief Calculates the product of two numbers.
    @param a The multiplicand.
    @param b The multiplier.
    @return The product of $a * b$.
    @raises TypeError If inputs are not numbers.
    """
    _validate_numbers(a, b)
    return _clean_result(a*b)

def div(a, b):
    """
    @brief Calculates the division of two numbers.
    @param a The dividend.
    @param b The divisor.
    @return The quotient of $a / b$.
    @raises TypeError If inputs are not numbers.
    @raises ZeroDivisionError If the divisor (b) is zero.
    """
    _validate_numbers(a, b)
    
    if (b == 0):
        raise ZeroDivisionError("Cannot divide by zero")
    
    return _clean_result(a/b)


def factorial(n):
    """
    @brief Calculates the factorial of a given number ($n!$).
    @param n A non-negative integer.
    @return The factorial of n.
    @raises TypeError If the input is not a number.
    @raises ValueError If n is negative or not an integer.
    @raises OverflowError If n exceeds MAX_FACTORIAL.
    """
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
    """
    @brief Raises a base to a given non-negative integer exponent.
    @details This function only supports non-negative integer exponents.
    @param base The base number.
    @param exponent The exponent (must be a non-negative integer).
    @return The result of $base^{exponent}$.
    @raises TypeError If inputs are not numbers.
    @raises ValueError If exponent is negative or not an integer.
    """
    _validate_numbers(base)
    
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
    """
    @brief Calculates the nth root of a base using the Newton-Raphson method.
    @param base The number to find the root of.
    @param degree The degree of the root ($n$).
    @return The calculated root.
    @raises TypeError If inputs are not numbers.
    @raises ValueError If degree is 0, if attempting an even root of a negative number, if the derivative reaches zero, or if it fails to converge within MAX_ITER.
    """
    _validate_numbers(base, degree)
    
    if degree == 0:
        raise ValueError("The root degree cannot be zero.")
    
    is_negative_degree = degree < 0
    # we can calculate the root of negative number only uneven number
    
    if base < 0 and degree % 2 == 0:
        raise ValueError("Cannot calc an even root of a neg num")
    
    if is_negative_degree:
        # Prevent 1 / 0 division errors mathematically
        if base == 0:
            raise ZeroDivisionError("Cannot calculate a negative root of zero.")
        degree = abs(degree)
        
    if base == 0:
        return 0
    
    if base == 1:
        return 1
    
    
    # Generate an automatic initial guess
    x_n = base / degree 
    
    for i in range(MAX_ITER):
        # Calculate f(x) and f'(x) based on the current guess
        f_x_n = (x_n ** degree) - base
        
        # Check if we are close enough to the true root
        if abs(f_x_n) < ROOT_TOL:
            
            if is_negative_degree:
                x_n = 1 / x_n
                
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
    """
    @brief Calculates the square of a number.
    @param a The number to be squared.
    @return The result of $a^2$.
    @raises TypeError If input is not a number.
    """
    _validate_numbers(a)
    
    return _clean_result(a*a)

def sqrt(a):
    """
    @brief Calculates the square root of a number.
    @details Implemented using the Babylonian method (a specific case of Newton's method).
    @param a The non-negative number to find the square root of.
    @return The square root of a.
    @raises TypeError If input is not a number.
    @raises ValueError If a is negative or if the method fails to converge.
    """
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
    """
    @brief (1/x) Returns ONE over X
    @param x The number to invert.
    @return The result of $1/x$.
    @raises TypeError If input is not a number.
    @raises ZeroDivisionError If x is zero.
    """
    _validate_numbers(x)
    
    if (x==0):
        raise ZeroDivisionError("Division by 0")
    
    return _clean_result(1/x)

