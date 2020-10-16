import unittest
from circles import circle_area
from math import pi

"todo run use python -m unittest or python -m unittest test_circles"


class TestCircleArea (unittest.TestCase):
    def test_area(self):
        # Test area when radiu >= 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)

    def test_values(self):
        # Make sure value errors are raised when neccesary
        self.assertRaises(ValueError, circle_area, -2)


    def test_types(self):
        # Make sure type errors are raised when neccesary
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "radius")
