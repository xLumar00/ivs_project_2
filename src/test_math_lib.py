## @file test_math_lib.py
#  @package test_math_lib
#  @brief Unit tests for the math_lib mathematical library.
#  @details Contains comprehensive test suites checking standard operations, 
#           boundary conditions, mathematical properties, and memory safety limits.
#  @author Timotej Lukotka | Absolute Zeros
#  @date 2026

import unittest
from math_lib import * 


## @class TestAddition
#  @brief Unit tests for the addition (add) function.
#  @details Verifies standard integer/float addition, zero cases, boundary conditions, 
#           invalid input exceptions, and algebraic properties (commutativity and associativity).
class TestAddition(unittest.TestCase):

    def test_standard_arithmetic(self):
        self.assertEqual(add(5, 7), 12)                  # Positive + Positive
        self.assertEqual(add(-3, -8), -11)               # Negative + Negative
        self.assertEqual(add(10, -4), 6)                 # Positive + Negative (Positive result)
        self.assertEqual(add(4, -10), -6)                # Positive + Negative (Negative result)
        self.assertEqual(add(2.5, 3.25), 5.75)           # Floats

    def test_zero_cases(self):
        self.assertEqual(add(8, 0), 8)                   # Positive + Zero
        self.assertEqual(add(-5, 0), -5)                 # Negative + Zero
        self.assertEqual(add(0, 0), 0)                   # Zero + Zero

    def test_boundaries_and_limits(self):
        self.assertEqual(add(0.1, 0.2), 0.3)
   
    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            add(5)  # Missing 'b'
        with self.assertRaises(TypeError):
            add("Five", 2)
        with self.assertRaises(TypeError):
            add("A", "B")
        with self.assertRaises(TypeError):
            add(None, 5)

    def test_mathematical_properties(self):
        a, b, c = 14, 8, 4
        # Commutative Property: a + b == b + a
        self.assertEqual(add(a, b), add(b, a))
        # Associative Property: (a + b) + c == a + (b + c)
        self.assertEqual(add(add(a, b), c), add(a, add(b, c)))       
                       

## @class TestSubtraction
#  @brief Unit tests for the subtraction (sub) function.
#  @details Verifies basic subtraction, subtraction involving zero, invalid types, 
#           float precision handling, and anti-commutative property.
class TestSubtraction(unittest.TestCase):

    def test_standard_arithmetic(self):
        self.assertEqual(sub(5, 3), 2)                  # Positive - Positive
        self.assertEqual(sub(-3, -8), 5)                 # Negative - Negative
        self.assertEqual(sub(10, -4), 14)                # Positive - Negative (Positive result)
        self.assertEqual(sub(-14, -10), -4)              # Positive - Negative (Negative result)
        self.assertEqual(sub(2.5, 3.25), -0.75)          # Floats
        
    def test_zero_cases(self):
        self.assertEqual(sub(8, 0), 8)                   # Positive + Zero
        self.assertEqual(sub(-5, 0), -5)                 # Negative + Zero
        self.assertEqual(sub(0, 0), 0)                   # Zero + Zero

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sub(5)  # Missing 'b'
        with self.assertRaises(TypeError):
            sub("Five", 2)
        with self.assertRaises(TypeError):
            sub("A", "B")
        with self.assertRaises(TypeError):
            sub(None, 5)
            
    def test_subtraction_floats(self):
        self.assertEqual(sub(0.3, 0.2), 0.1)
        
    def test_subtraction_properties(self):
        a, b = 15, 8
        self.assertEqual(sub(a, b), -sub(b, a))
        

## @class TestMultiplication
#  @brief Unit tests for the multiplication (mul) function.
#  @details Verifies basic multiplication, identity laws, zero multiplication, 
#           commutativity, and invalid input safety.
class TestMultiplication(unittest.TestCase):

    def test_multiplication_standard(self):
        self.assertEqual(mul(5, 6), 30)            # Positive * Positive
        self.assertEqual(mul(-4, -4), 16)          # Negative * Negative
        self.assertEqual(mul(7, -3), -21)          # Mixed signs

    def test_multiplication_zero(self):
        self.assertEqual(mul(9, 0), 0)             # Multiply by zero
        self.assertEqual(mul(0, 0), 0)             # Zero * Zero
        
    def test_multiplication_identity(self):
        self.assertEqual(mul(14, 1), 14)           # Identity property (Multiply by 1)
        self.assertEqual(mul(14, -1), -14)         # Multiply by -1

    def test_multiplication_properties(self):
        self.assertEqual(mul(6, 7), mul(7, 6))
    
    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            mul(5)  # Missing 'b'
        with self.assertRaises(TypeError):
            mul("Five", 2)
        with self.assertRaises(TypeError):
            mul("A", "B")
        with self.assertRaises(TypeError):
            mul(None, 5)
            

## @class TestDivision
#  @brief Unit tests for the division (div) function.
#  @details Verifies exact division, division by zero exceptions, identity laws, 
#           float outputs, and type validation.
class TestDivision(unittest.TestCase):

    def test_division_standard(self):
        self.assertEqual(div(20, 4), 5)            # Clean division
        self.assertEqual(div(-15, -3), 5)          # Negative / Negative
        self.assertEqual(div(16, -2), -8)          # Mixed signs
        self.assertEqual(div(5, 2), 2.5)           # Division resulting in float

    def test_division_zero_cases(self):
        self.assertEqual(div(0, 8), 0)             # Zero divided by a number is 0
        with self.assertRaises(ZeroDivisionError):
            div(8, 0)
        with self.assertRaises(ZeroDivisionError):
            div(0, 0)

    def test_division_identity(self):
        self.assertEqual(div(42, 1), 42)           # Divide by 1
        self.assertEqual(div(42, -1), -42)         # Divide by -1

    def test_division_floats(self):
        self.assertEqual(div(1, 3), 0.333333333)
        
    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            div(5)  # Missing 'b'
        with self.assertRaises(TypeError):
            div("Five", 2)
        with self.assertRaises(TypeError):
            div("A", "B")
        with self.assertRaises(TypeError):
            div(None, 5)
            

## @class TestFactorial
#  @brief Unit tests for the factorial function.
#  @details Verifies natural number factorials, zero case, negative boundary exceptions, 
#           invalid float types, and memory-safety overflows.
class TestFactorial(unittest.TestCase):

    def test_standard_factorial(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(5), 120)       
        self.assertEqual(factorial(10), 3628800)
        
    def test_zero_factorial(self):
        self.assertEqual(factorial(0), 1)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            factorial(-5)

    def test_floats_and_decimals(self):
        with self.assertRaises(ValueError):
            factorial(3.5)
            
    def test_overflow_threshold(self):
        self.assertEqual(factorial(64), 126886932185884164103433389335161480802865516174545192198801894375214704230400000000000000)
        self.assertGreater(factorial(MAX_FACTORIAL), 0)
        with self.assertRaises(OverflowError):
            factorial(1001)
            

## @class TestPower
#  @brief Unit tests for the exponentiation (power) function.
#  @details Verifies integer and decimal bases, negative bases, zero cases, 
#           natural exponent constraints, type validation, and power limits.
class TestPower(unittest.TestCase):

    def test_float_bases(self):
        # Validation of exponentiation with decimal numbers (decimal base)
        self.assertEqual(power(1.5, 2), 2.25)
        self.assertEqual(power(2.5, 3), 15.625)
        self.assertEqual(power(0.5, 4), 0.0625)

    def test_standard_power(self):
        self.assertEqual(power(2, 3), 8)           # 2^3 = 8
        self.assertEqual(power(5, 2), 25)          # 5^2 = 25
        self.assertEqual(power(10, 4), 10000)      # 10^4 = 10000
        self.assertEqual(power(2, 1), 2)           # Power of 1 returns the base

    def test_negative_bases(self):
        self.assertEqual(power(-3, 2), 9)          
        self.assertEqual(power(-3, 3), -27)        
    
    def test_zero_exponent(self):
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(-10, 0), 1)
        self.assertEqual(power(0, 0), 1)         
        
    def test_zero_base(self):
        self.assertEqual(power(0, 5), 0)

    def test_negative_exponents(self):
        with self.assertRaises(ValueError):
            power(2, -2)

    def test_float_exponents(self):
        with self.assertRaises(ValueError):
            power(4, 2.5)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            power("two", 3)
        with self.assertRaises(TypeError):
            power(2, None)

    def test_power_overflow(self):
        with self.assertRaises(OverflowError):
            power(2, 1001)
            

## @class TestSquare
#  @brief Unit tests for the squaring (square) function.
#  @details Verifies squaring positive, negative, zero, and decimal/float numbers.
class TestSquare(unittest.TestCase):

    def test_standard_square(self):
        self.assertEqual(square(4), 16)
        self.assertEqual(square(10), 100)
        
    def test_negative_square(self):
        self.assertEqual(square(-5), 25)
        self.assertEqual(square(-1), 1)

    def test_zero_square(self):
        self.assertEqual(square(0), 0)

    def test_float_square(self):
        self.assertEqual(square(1.5), 2.25)
        self.assertEqual(square(-2.5), 6.25)


## @class TestRoot
#  @brief Unit tests for the nth root function.
#  @details Verifies standard roots, 0 and 1 base edge cases, math violations (even root 
#           of negative, 0th root), odd roots of negative bases, negative degree roots, 
#           and division by zero traps.
class TestRoot(unittest.TestCase):

    def test_standard_roots(self):
        self.assertEqual(root(9, 2), 3.0)      
        self.assertEqual(root(27, 3), 3.0)     
        self.assertEqual(root(16, 4), 2.0)     
        self.assertEqual(root(32, 5), 2.0)     

    def test_zero_and_one_base(self):
        self.assertEqual(root(0, 5), 0)            
        self.assertEqual(root(1, 5), 1)            

    def test_zero_degree(self):
        with self.assertRaises(ValueError):
            root(25, 0)

    def test_even_root_of_negative(self):
        with self.assertRaises(ValueError):
            root(-16, 2)
        with self.assertRaises(ValueError):
            root(-81, 4)

    def test_odd_root_of_negative(self):
        self.assertEqual(root(-27, 3), -3.0)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            root("nine", 2)
    
    def test_standard_negative_root(self):
        self.assertEqual(root(8, -3), 0.5)

    def test_even_negative_root(self):
        self.assertEqual(root(16, -2), 0.25)
    
    def test_negative_base_negative_odd_root(self):
        self.assertEqual(root(-32, -5), -0.5)
    
    def test_zero_trap_raises_error(self):
        with self.assertRaises(ZeroDivisionError):
            root(0, -2)
        with self.assertRaises(ZeroDivisionError):
            root(0, -3)


## @class TestSqrt
#  @brief Unit tests for the square root (sqrt) function.
#  @details Verifies typical square roots, floating-point results, zero base, 
#           negative-base validation, and invalid type safety.
class TestSqrt(unittest.TestCase):

    def test_standard_sqrt(self):
        self.assertEqual(sqrt(25), 5.0)
        self.assertEqual(sqrt(144), 12.0)
        
    def test_float_sqrt(self):
        self.assertEqual(sqrt(2.25), 1.5)

    def test_zero_sqrt(self):
        self.assertEqual(sqrt(0), 0)

    def test_negative_sqrt(self):
        with self.assertRaises(ValueError):
            sqrt(-4)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            sqrt(None)


## @class TestInverse
#  @brief Unit tests for the reciprocal (inverse) function.
#  @details Verifies standard inverse values, negative inverses, float inverses, 
#           division by zero exceptions, and type checking.
class TestInverse(unittest.TestCase):

    def test_standard_inverse(self):
        self.assertEqual(inverse(2), 0.5)          
        self.assertEqual(inverse(4), 0.25)         
        self.assertEqual(inverse(10), 0.1)         

    def test_negative_inverse(self):
        self.assertEqual(inverse(-2), -0.5)        
        self.assertEqual(inverse(-4), -0.25)

    def test_float_inverse(self):
        self.assertEqual(inverse(0.5), 2.0)        
        self.assertEqual(inverse(0.25), 4.0)       

    def test_zero_inverse(self):
        with self.assertRaises(ZeroDivisionError):
            inverse(0)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            inverse("text")


## @class TestSafetyAndLimits
#  @brief Safety and memory limit test cases for the library.
#  @details Validates that inputs exceeding MAX_SAFE_INPUT correctly trigger 
#           OverflowError to prevent system memory overload.
class TestSafetyAndLimits(unittest.TestCase):

    def test_maximum_safe_input_overflow(self):
        with self.assertRaises(OverflowError):
            add(1e101, 1)
        with self.assertRaises(OverflowError):
            sub(-1e101, 1)
        with self.assertRaises(OverflowError):
            mul(1e101, 2)
        with self.assertRaises(OverflowError):
            div(1e101, 2)


if __name__ == '__main__':
    unittest.main()
