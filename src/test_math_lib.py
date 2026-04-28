import unittest
from math_lib import * 

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
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)
   
    def test_invalid_inputs(self):
        # Missing Argument 
        with self.assertRaises(TypeError):
            add(5)  # Missing 'b'

        # Text/Strings
        with self.assertRaises(TypeError):
            add("Five", 2)
            
        with self.assertRaises(TypeError):
            add("A", "B")

        # Null/None values
        with self.assertRaises(TypeError):
            add(None, 5)

    def test_mathematical_properties(self):
        a, b, c = 14, 8, 4

        # Commutative Property: a + b == b + a
        self.assertEqual(add(a, b), add(b, a))

        # Associative Property: (a + b) + c == a + (b + c)
        self.assertEqual(add(add(a, b), c), add(a, add(b, c)))       
                       
class TestSubtraction(unittest.TestCase):
    def test_standard_arithmetic(self):
        self.assertEqual(sub(5, 3),2 )                 # Positive - Positive
        self.assertEqual(sub(-3, -8), 5)               # Negative - Negative
        self.assertEqual(sub(10, -4), 14)              # Positive - Negative (Positive result)
        self.assertEqual(sub(-14, -10), -4)            # Positive - Negative (Negative result)
        self.assertEqual(sub(2.5, 3.25), -0.75)        # Floats
        
    def test_zero_cases(self):
        self.assertEqual(sub(8, 0), 8)                 # Positive + Zero
        self.assertEqual(sub(-5, 0), -5)               # Negative + Zero
        self.assertEqual(sub(0, 0), 0)                 # Zero + Zero

    def test_invalid_inputs(self):
        # Missing Argument 
        with self.assertRaises(TypeError):
            sub(5)  # Missing 'b'

        # Text/Strings
        with self.assertRaises(TypeError):
            sub("Five", 2)
            
        with self.assertRaises(TypeError):
            sub("A", "B")

        # Null/None values
        with self.assertRaises(TypeError):
            sub(None, 5)
            
    def test_subtraction_floats(self):
    
        self.assertAlmostEqual(sub(0.3, 0.2), 0.1, places=7)
        
    def test_subtraction_properties(self):
        a, b = 15, 8
        self.assertEqual(sub(a, b), -sub(b, a))
        
class TestMultiplication(unittest.TestCase):
    def test_multiplication_standard(self):
    
        self.assertEqual(mul(5, 6), 30)            # Positive * Positive
        self.assertEqual(mul(-4, -4), 16)          # Negative * Negative (Result positive)
        self.assertEqual(mul(7, -3), -21)          # Mixed signs (Result negative)

    def test_multiplication_zero(self):
    
        self.assertEqual(mul(9, 0), 0)             # Multiply by zero
        self.assertEqual(mul(0, 0), 0)             # Zero * Zero
        
    def test_multiplication_identity(self):
        self.assertEqual(mul(14, 1), 14)           # Identity property (Multiply by 1)
        self.assertEqual(mul(14, -1), -14)         # Multiply by -1

    def test_multiplication_properties(self):
        # Commutative: a * b == b * a
        self.assertEqual(mul(6, 7), mul(7, 6))
    
    def test_invalid_inputs(self):
        
        with self.assertRaises(TypeError):
            mul(5)  # Missing 'b'
            
        # Text/Strings
        with self.assertRaises(TypeError):
            mul("Five", 2)
            
        with self.assertRaises(TypeError):
            mul("A", "B")
            
        # Null/None values
        with self.assertRaises(TypeError):
            mul(None, 5)
            
class TestDivision(unittest.TestCase):
    
    def test_division_standard(self):
        self.assertEqual(div(20, 4), 5)            # Clean division
        self.assertEqual(div(-15, -3), 5)          # Negative / Negative
        self.assertEqual(div(16, -2), -8)          # Mixed signs
        self.assertEqual(div(5, 2), 2.5)           # Division resulting in float

    def test_division_zero_cases(self):
        self.assertEqual(div(0, 8), 0)             # Zero divided by a number is 0
        
        #Division by zero 
        with self.assertRaises(ZeroDivisionError):
            div(8, 0)
        with self.assertRaises(ZeroDivisionError):
            div(0, 0)

    def test_division_identity(self):

        self.assertEqual(div(42, 1), 42)           # Divide by 1
        self.assertEqual(div(42, -1), -42)         # Divide by -1

    def test_division_floats(self):
        
        self.assertAlmostEqual(div(1, 3), 0.3333333, places=7)
        
    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            div(5)  # Missing 'b'

        # Text/Strings
        with self.assertRaises(TypeError):
            div("Five", 2)
        with self.assertRaises(TypeError):
            div("A", "B")

        # Null/None values
        with self.assertRaises(TypeError):
            div(None, 5)
            
class TestFactorial(unittest.TestCase):

    # Standard tests
    def test_standard_factorial(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(5), 120)       
        self.assertEqual(factorial(10), 3628800)

    
    def test_zero_factorial(self):
        #0! == 1
        self.assertEqual(factorial(0), 1)

    # Error check
    def test_negative_numbers(self):
        # Factorials are  only for non-negative integers. 
        
        with self.assertRaises(ValueError):
            factorial(-5)

    def test_floats_and_decimals(self):
        # Standard factorials do not apply to fractions/decimals.
        with self.assertRaises(ValueError):
            factorial(3.5)

class TestPower(unittest.TestCase):

    # Standard tests
    def test_standard_power(self):
        self.assertEqual(power(2, 3), 8)           # 2^3 = 8
        self.assertEqual(power(5, 2), 25)          # 5^2 = 25
        self.assertEqual(power(10, 4), 10000)      # 10^4 = 10000
        self.assertEqual(power(2, 1), 2)           # Power of 1 returns the base

    # Negative Bases
    def test_negative_bases(self):
        # A negative base to an even power becomes positive
        self.assertEqual(power(-3, 2), 9)          
        # A negative base to an odd power stays negative
        self.assertEqual(power(-3, 3), -27)        
    
        # Zero cases
    def test_zero_exponent(self):
        # Anything to the power of 0 is 1
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(-10, 0), 1)
        self.assertEqual(power(0, 0), 1)         
        
    def test_zero_base(self):
        # 0 to any positive power is 0
        self.assertEqual(power(0, 5), 0)

    # Errors check (The "Natural Exponents Only" Rule)
    def test_negative_exponents(self):
        with self.assertRaises(ValueError):
            power(2, -2)

    def test_float_exponents(self):
        # 2.5 is not a natural number.
        with self.assertRaises(ValueError):
            power(4, 2.5)

    # Invalid Types
    def test_invalid_types(self):
        # Proves _validate_numbers is working
        with self.assertRaises(TypeError):
            power("two", 3)
        with self.assertRaises(TypeError):
            power(2, None)
            
class TestSquare(unittest.TestCase):

    # Standard tests
    def test_standard_square(self):
        self.assertEqual(square(4), 16)
        self.assertEqual(square(10), 100)
        
    # Negative numbers
    def test_negative_square(self):
        # A negative times a negative is always positive
        self.assertEqual(square(-5), 25)
        self.assertEqual(square(-1), 1)

    def test_zero_square(self):
        self.assertEqual(square(0), 0)

    # floats
    def test_float_square(self):
        self.assertAlmostEqual(square(1.5), 2.25)
        self.assertAlmostEqual(square(-2.5), 6.25)

class TestRoot(unittest.TestCase):

    # standard tests
    def test_standard_roots(self):
        self.assertAlmostEqual(root(9, 2), 3.0, places=7)      # Square root
        self.assertAlmostEqual(root(27, 3), 3.0, places=7)     # Cube root
        self.assertAlmostEqual(root(16, 4), 2.0, places=7)     # 4th root
        self.assertAlmostEqual(root(32, 5), 2.0, places=7)     # 5th root

    def test_zero_and_one_base(self):
        self.assertEqual(root(0, 5), 0)            # Any root of 0 is 0
        self.assertEqual(root(1, 5), 1)            # Any root of 1 is 1

    # Invalid math
    def test_zero_degree(self):
        # The 0th root of a number is mathematically undefined
        with self.assertRaises(ValueError):
            root(25, 0)

    def test_even_root_of_negative(self):
        # In real numbers, you cannot take an even root (like a square root) of a negative number.
        with self.assertRaises(ValueError):
            root(-16, 2)
        with self.assertRaises(ValueError):
            root(-81, 4)

    #  The "Odd Root of a Negative" Case
    def test_odd_root_of_negative(self):
    
        self.assertAlmostEqual(root(-27, 3), -3.0, places=5)

    #  Invalid Types
    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            root("nine", 2)


class TestSqrt(unittest.TestCase):

    def test_standard_sqrt(self):
        self.assertAlmostEqual(sqrt(25), 5.0, 5)
        self.assertAlmostEqual(sqrt(144), 12.0, 5)
        
    def test_float_sqrt(self):
        self.assertAlmostEqual(sqrt(2.25), 1.5, 5)

    def test_zero_sqrt(self):
        self.assertEqual(sqrt(0), 0)

    def test_negative_sqrt(self):
        # Square root is an even root (degree 2), so negatives must be blocked
        with self.assertRaises(ValueError):
            sqrt(-4)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            sqrt(None)


class TestInverse(unittest.TestCase):

    # 1. Standard tests
    def test_standard_inverse(self):
        self.assertEqual(inverse(2), 0.5)          # 1 / 2
        self.assertEqual(inverse(4), 0.25)         # 1 / 4
        self.assertEqual(inverse(10), 0.1)         # 1 / 10

    # 2. Negative Numbers
    def test_negative_inverse(self):
        self.assertEqual(inverse(-2), -0.5)        # 1 / -2
        self.assertEqual(inverse(-4), -0.25)

    # 3. Decimal/Float Inputs
    def test_float_inverse(self):
        self.assertEqual(inverse(0.5), 2.0)        # 1 / 0.5 = 2
        self.assertEqual(inverse(0.25), 4.0)       # 1 / 0.25 = 4

    # 4. The Zero Case 
    def test_zero_inverse(self):
        # The inverse of 0 is mathematically undefined (1 / 0). 
        # Your function MUST catch this and raise a ZeroDivisionError.
        with self.assertRaises(ZeroDivisionError):
            inverse(0)

    # 5. Invalid Types
    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            inverse("text")
    
class TestMathLib(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,2),4)
      
    def test_sub(self):
        self.assertEqual(sub(5, 10), -5)
     
    def test_mul(self):
        self.assertEqual(mul(2,2) , 4 )
    
    def test_div(self):
        self.assertEqual(div(4,2), 2)
    
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_root(self):
        self.assertAlmostEqual(root(27,3), 3, 7)

    def test_square(self):
        self.assertEqual(square(4), 16)

    def test_sqrt(self):
        self.assertEqual(sqrt(25), 5)
    
    def test_inverse(self):
        self.assertEqual(inverse(4), 0.25)
        

if __name__ == '__main__':
    unittest.main()