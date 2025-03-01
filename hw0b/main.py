"""
method and unit test for triangle classification
"""

import unittest

def classify_triangle(a, b, c):
    """determine if the given 3 numbers can form a triangle"""

    return_string = ""

    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid lengths"

    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid triangle"

    if a == b and b == c:
        return_string += "equilateral, "
    elif a == b or b == c or a == c:
        return_string += "isosceles, "
    else:
        return_string += "scalene, "

    if a*a + b*b == c*c:
        return_string += "is a right triangle"
    else:
        return_string += "is not a right triangle"

    return return_string

class TestTriangle(unittest.TestCase):
    """test cases for the classify_triangle function"""
    def test_equilateral(self):
        """test equilateral triangle"""
        self.assertEqual(classify_triangle(2, 2, 2), "equilateral, is not a right triangle")
    def test_isosceles(self):
        """test isosceles triangle"""
        self.assertEqual(classify_triangle(3, 3, 5), "isosceles, is not a right triangle")
    def test_scalene(self):
        """test scalene triangle"""
        self.assertEqual(classify_triangle(4, 3, 5), "scalene, is a right triangle")
    def test_not_triangle(self):
        """test invalid triangle"""
        self.assertEqual(classify_triangle(3, 3, 50), "Invalid triangle")
    def test_not_triangle2(self):
        """test invalid inputs"""
        self.assertEqual(classify_triangle(-3, -4, -5), "Invalid lengths")
    def test_stress(self):
        """stress test"""
        self.assertEqual(classify_triangle(100, 100, 180), "isosceles, is not a right triangle")

if __name__ == '__main__':
    unittest.main()

