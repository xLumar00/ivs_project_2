## @file math_lib.py
#  @package math_lib
#  @brief Mathematical library for the IVS calculator project.
#  @details Contains basic arithmetic operations and advanced functions such as factorial, 
#           exponentiation, roots (Newton-Raphson method), and helper validation functions.
#  @author Timotej Lukotka | Absolute Zeros
#  @date 2026

#Formatting precision
SNAP_TOL = 1e-7  
MAX_DECIMAL_PLACES = 9

# Algorithmic precision
ROOT_TOL = 1e-10 
MAX_ITER = 100
# Memory Safety
MAX_FACTORIAL = 1000
MAX_SAFE_INPUT = 1e100


## @brief Validates that all provided arguments are either integers or floats.
#  @details This is an internal helper function used to ensure type safety across the library.
#  @param args Variable length argument list of values to check.
#  @raises TypeError If any argument in args is not of type int or float.
#  @raises OverflowError If any argument exceeds MAX_SAFE_INPUT.
def _validate_numbers(*args):
    for arg in args:
        if  not isinstance(arg, (int, float)):
            raise TypeError("Inputs must be numbers")
        if abs(arg) > MAX_SAFE_INPUT:
            raise OverflowError("Input number is too large for this calculator.")


## @brief Cleans up a numerical result to handle floating-point precision issues.
#  @details This internal helper function performs two formatting tasks:
#           1. Snaps the result to the nearest integer if it is within SNAP_TOL.
#           2. Otherwise, rounds the result to MAX_DECIMAL_PLACES to eliminate 
#              common floating-point arithmetic artifacts.
#  @param result The numerical value to be cleaned.
#  @return The cleaned numerical result (either an int or a rounded float).
def _clean_result(result):
    round_result = round(result)
    if abs(result - round_result) < SNAP_TOL:
        return round_result
    #round numbers outside of needed decimal precision(7decimals) so 0.3 - 0.2 = 0.1 not 0.0999...
    return round(result,MAX_DECIMAL_PLACES)
    

## @brief Calculates the sum of two numbers.
#  @param a The first number.
#  @param b The second number.
#  @return The sum of a + b.
#  @raises TypeError If inputs are not numbers.
def add(a, b):
    _validate_numbers(a, b)
    return _clean_result(a+b)


## @brief Calculates the difference between two numbers.
#  @param a The minuend.
#  @param b The subtrahend.
#  @return The difference of a - b.
#  @raises TypeError If inputs are not numbers.
def sub(a, b):
    _validate_numbers(a, b)
    return _clean_result(a-b)


## @brief Calculates the product of two numbers.
#  @param a The multiplicand.
#  @param b The multiplier.
#  @return The product of a * b.
#  @raises TypeError If inputs are not numbers.
def mul(a, b):
    _validate_numbers(a, b)
    return _clean_result(a*b)


## @brief Calculates the division of two numbers.
#  @param a The dividend.
#  @param b The divisor.
#  @return The quotient of a / b.
#  @raises TypeError If inputs are not numbers.
#  @raises ZeroDivisionError If the divisor (b) is zero.
def div(a, b):
    _validate_numbers(a, b)
    
    if (b == 0):
        raise ZeroDivisionError("Cannot divide by zero")
    
    return _clean_result(a/b)


## @brief Calculates the factorial of a given number (n!).
#  @param n A non-negative integer.
#  @return The factorial of n.
#  @raises TypeError If the input is not a number.
#  @raises ValueError If n is negative or not an integer.
#  @raises OverflowError If n exceeds MAX_FACTORIAL.
def factorial(n):
    _validate_numbers(n) 
    if (n < 0) : 
        raise ValueError("n! not defined for negative values")
    
    if isinstance(n, float) and n.is_integer():
        n = int(n)
        
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


## @brief Raises a base to a given non-negative integer exponent.
#  @details This function only supports non-negative integer exponents.
#  @param base The base number.
#  @param exponent The exponent (must be a non-negative integer).
#  @return The result of base^exponent.
#  @raises TypeError If inputs are not numbers.
#  @raises ValueError If exponent is negative or not an integer.
#  @raises OverflowError If exponent exceeds 1000.
def power(base, exponent):
    _validate_numbers(base)
    
    if (0 > exponent) : 
        raise ValueError("Exponent must be natural numbers or 0")
    
    if isinstance(exponent, float) and exponent.is_integer():
        exponent = int(exponent)
    
    if not (isinstance(exponent, int)):
        raise ValueError("Exponent must be natural numbers or 0")
    
    if exponent > 1000: # Adjust this limit based on your needs
        raise OverflowError("Exponent is too large")
    
    if exponent == 0:
        return 1
    
    counter = 1
    result = base
    
    for counter in range(1,exponent):
        result *= base
       
    return _clean_result(result)


## @brief Calculates the nth root of a base using the Newton-Raphson method.
#  @param base The number to find the root of.
#  @param degree The degree of the root (n).
#  @return The calculated root.
#  @raises TypeError If inputs are not numbers.
#  @raises ValueError If degree is 0, if attempting an even root of a negative number, if the derivative reaches zero, or if it fails to converge.
#  @raises ZeroDivisionError If attempting a negative root of zero.
def root(base, degree):
    _validate_numbers(base, degree)
    
    if degree == 0:
        raise ValueError("The root degree cannot be zero.")
    
    is_negative_degree = degree < 0
    
    if base < 0 and degree % 2 == 0:
        raise ValueError("Cannot calc an even root of a neg num")
    
    if is_negative_degree:
        if base == 0:
            raise ZeroDivisionError("Cannot calculate a negative root of zero.")
        degree = abs(degree)
        
    if base == 0:
        return 0
    
    if base == 1:
        return 1
    
    x_n = base / degree 
    
    for i in range(MAX_ITER):
        f_x_n = (x_n ** degree) - base
        
        if abs(f_x_n) < ROOT_TOL:
            if is_negative_degree:
                x_n = 1 / x_n
            return _clean_result(x_n)
            
        df_x_n = degree * (x_n ** (degree - 1))
        
        if df_x_n == 0:
            raise ValueError("MathError:Div by 0 during root calc.")
            
        x_n = x_n - (f_x_n / df_x_n)
        
    raise ValueError("Calculation took too long stopped")


## @brief Calculates the square of a number.
#  @param a The number to be squared.
#  @return The result of a^2.
#  @raises TypeError If input is not a number.
def square(a):
    _validate_numbers(a)
    return _clean_result(a*a)


## @brief Calculates the square root of a number.
#  @details Implemented using the Babylonian method (Newton's method case).
#  @param a The non-negative number to find the square root of.
#  @return The square root of a.
#  @raises TypeError If input is not a number.
#  @raises ValueError If a is negative or if the method fails to converge.
def sqrt(a):
    _validate_numbers(a)
    if a < 0:
        raise ValueError("Cannot calculate the sqrt of a neg number")
    
    if a == 0:
        return 0 
    
    x_n = a/2
    prev_x_n = 0
    
    for i in range(MAX_ITER):
        prev_x_n =  x_n
        x_n = 1/2 * (x_n + a/x_n)
        if abs(x_n - prev_x_n) < ROOT_TOL:
            return _clean_result(x_n)

    raise ValueError


## @brief Returns ONE over X (1/x).
#  @param x The number to invert.
#  @return The result of 1/x.
#  @raises TypeError If input is not a number.
#  @raises ZeroDivisionError If x is zero.
def inverse(x):
    _validate_numbers(x)
    
    if (x==0):
        raise ZeroDivisionError("Division by 0")
    
    return _clean_result(1/x)
