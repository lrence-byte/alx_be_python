#simple_calculator.py

class SimpleCalculator:
    """A simple calculator class that supports basic arithmetic operations."""

    def add(self, a, b):
        """Return the addition of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the subtraction of b from a."""
        return a - b

    def multiply(self, a, b):
        """Return the multiplication of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the division of a by b. Returns None if b is zero."""
        if b == 0:
            return None
        return a / b

# import unittest
# from test_simple_calculator import SimpleCalculator

# class TestSimpleCalculator(unittest.TestCase):

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.add(2, 3), 5)       
        self.assertEqual(self.add(-1, 1), 0)      
        self.assertEqual(self.add(0, 0), 0)        
        self.assertEqual(self.add(-5, -3), -8)     
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.subtract(5, 3), 2)   
        self.assertEqual(self.subtract(-1, 1), -2)  
        self.assertEqual(self.subtract(0, 0), 0)    
        self.assertEqual(self.subtract(-5, -3), -2) 

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.multiply(2, 3), 6)   
        self.assertEqual(self.multiply(-1, 5), -5)  
        self.assertEqual(self.multiply(0, 5), 0)    
        self.assertEqual(self.multiply(-2, -4), 8) 

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.divide(6, 2), 3)      
        self.assertEqual(self.divide(-6, 2), -3)      
        self.assertEqual(self.divide(5, 2), 2.5)     
        self.assertEqual(self.divide(0, 1), 0)       
        self.assertEqual(self.divide(5, 0), None)    

# if __name__ == '__main__':
#     unittest.main()

import unittest
from test_simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.add(2, 3), 5)       
        self.assertEqual(self.add(-1, 1), 0)      
        self.assertEqual(self.add(0, 0), 0)        
        self.assertEqual(self.add(-5, -3), -8)     
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.subtract(5, 3), 2)   
        self.assertEqual(self.subtract(-1, 1), -2)  
        self.assertEqual(self.subtract(0, 0), 0)    
        self.assertEqual(self.subtract(-5, -3), -2) 

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.multiply(2, 3), 6)   
        self.assertEqual(self.multiply(-1, 5), -5)  
        self.assertEqual(self.multiply(0, 5), 0)    
        self.assertEqual(self.multiply(-2, -4), 8) 

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.divide(6, 2), 3)      
        self.assertEqual(self.divide(-6, 2), -3)      
        self.assertEqual(self.divide(5, 2), 2.5)     
        self.assertEqual(self.divide(0, 1), 0)       
        self.assertEqual(self.divide(5, 0), None)    


        if __name__ == '__main__':
            unittest.main()