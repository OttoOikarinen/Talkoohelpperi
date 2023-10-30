import unittest
from unittest.mock import patch
import talkoohelpperi

sum = talkoohelpperi.sum

class TestSum(unittest.TestCase):
    def test_sum(self):
        a = 2
        b = 3
        result = sum(a, b)
        self.assertEqual(result, 5)
    
    def test_failing(self):
        a = 5
        b = 10
        result = a + b
        self.assertEqual(result, 15)


if __name__ == '__main__':
    unittest.main()
    print("Everything passed!")