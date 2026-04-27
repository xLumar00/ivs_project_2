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
        self.assertEqual(root(27, 3), 3)

    def test_square(self):
        self.assertEqual(square(4), 16)

    def test_sqrt(self):
        self.assertEqual(sqrt(25), 5)
    
    def test_inverse(self):
        self.assertEqual(inverse(4), 0.25)
        

if __name__ == '__main__':
    unittest.main()