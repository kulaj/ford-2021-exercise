import unittest
from manhattan import Point, compute_manhattan_distance, is_numeric

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
        self.assertFalse(is_numeric(" "))
    
    def test_manhattan_dist_simple(self):
        p1 = Point(1,1)
        p2 = Point(2,2)
        self.assertAlmostEqual(compute_manhattan_distance(p1, p2), 2)

    def test_manhattan_dist_fraction(self):
        p1 = Point(3,3.5)
        p2 = Point(5.1,5.2)
        self.assertAlmostEqual(compute_manhattan_distance(p1, p2), 3.8)

    def test_manhattan_dist_zero(self):
        p1 = Point(0,0)
        p2 = Point(0,0)
        self.assertAlmostEqual(compute_manhattan_distance(p1, p2), 0)

    def test_manhattan_dist_negative(self):
        p1 = Point(3,3.5)
        p2 = Point(-5.1,-5.2)
        self.assertAlmostEqual(compute_manhattan_distance(p1, p2), 16.8)

    

if __name__ == '__main__':
    unittest.main()