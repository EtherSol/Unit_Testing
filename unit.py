import unittest
import calc

class TestCalc(unittest.TestCase):
    
    def test_add(self): 
        result = calc.add(10,4)
        self.assertEqual(result,14)


if __name__ == '__main__':
    unittest.main()