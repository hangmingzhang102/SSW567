import unittest

def classify_triangle(a, b, c):
    returnString = ""

    if(a + b <= c or a + c <= b or b + c <= a):
        return "Invalid triangle"

    if(a == b and b == c):
        returnString += "equilateral, "
    elif(a == b or b == c or a == c):
        returnString += "isosceles, "
    else:
        returnString += "scalene, "

    if(a*a + b*b == c*c):
        returnString += "is a right triangle"
    else:
        returnString += "is not a right triangle"

    return returnString

class TestTriangle(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(classify_triangle(2, 2, 2), "equilateral, is not a right triangle")
    def test_isosceles(self):
        self.assertEqual(classify_triangle(3, 3, 5), "isosceles, is not a right triangle")
    def test_scalene(self):
        self.assertEqual(classify_triangle(4, 3, 5), "scalene, is a right triangle")
    def test_not_triangle(self):
        self.assertEqual(classify_triangle(3, 3, 50), "Invalid triangle")
    def test_stress(self):
        self.assertEqual(classify_triangle(100, 100, 180), "isosceles, is not a right triangle")

if __name__ == '__main__':
    unittest.main()

