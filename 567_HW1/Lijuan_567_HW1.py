import unittest


def triangle_clarification(a, b, c):
    if a == b == c:

        triangle_type = "equailateral"

    elif a == b or b == c or a == c:
        triangle_type = "isosceles"

    else:
        triangle_type = "escalene"

    if a**2 + b**2 == c**2 or b**2+c**2 == a**2 or a**2 + c**2 == b**2:
        right_triangle = "right"
    else:
        right_triangle = "not right"


class TestTriangleClarification(unittest.TestCase):

    def test_equilateral_triangle(self):
      
        result = triangle_clarification(3, 3, 3)
        self.assertEqual(result, "Equilateral right")

    def test_isosceles_triangle(self):
       
        result = triangle_clarification(4, 4, 5)
        self.assertEqual(result, "Isosceles not right")

    def test_scalene_triangle(self):
      
        result = triangle_clarification(3, 4, 5)
        self.assertEqual(result, "Scalene right")

    def test_right_triangle(self):
      
        result = triangle_clarification(6, 8, 10)
        self.assertEqual(result, "Scalene right")

    def test_not_a_triangle(self):
     
        result = triangle_clarification(1, 2, 3)
        self.assertEqual(result, "Not a triangle")

    def test_negative_sides(self):

        result = triangle_clarification(-3, 4, 5)
        self.assertEqual(result, "Not a triangle")

    def test_zero_sides(self):
    
        result = triangle_clarification(0, 6, 4)
        self.assertEqual(result, "Not a triangle")

    def test_large_values(self):

        result = triangle_clarification(1540000, 1550001, 2500000)
        self.assertEqual(result, "Scalene right")

if __name__ == '__main__':
    unittest.main()
