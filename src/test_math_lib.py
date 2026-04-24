import unittest
from math_lib import * 
                                                    

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