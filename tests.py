import unittest
from manhattan import compute_manhattan_distance, is_numeric

class TestManhattenDistance(unittest.TestCase):

    def test_is_numeric_basic(self):
        self.assertTrue(is_numeric("5"))

    def test_is_numeric_decimal(self):
        self.assertTrue(is_numeric("5.3"))

    def test_is_numeric_negative(self):
        self.assertTrue(is_numeric("-5"))

    def test_is_numeric_zero(self):
        self.assertTrue(is_numeric("0"))

    def test_is_numeric_random_string(self):
        self.assertFalse(is_numeric("ford motor company"))

    def test_is_numeric_whitespace(self):
        self.assertFalse(is_numeric("ford motor company"))

    

if __name__ == '__main__':
    unittest.main()