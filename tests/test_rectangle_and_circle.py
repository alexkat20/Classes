import unittest
from Task3 import Circle, Rectangle


class TestRectangle(unittest.TestCase):
    PI = 3.14

    def test_rectangle_square(self):
        rect = Rectangle(10, 20)
        assert rect.calculate_square() == 200

    def test_rectangle_perimeter(self):
        rect = Rectangle(10, 20)
        assert rect.calculate_perimeter() == 60

    def test_circle_square(self):
        circle = Circle(10)
        assert circle.calculate_square() == self.PI * 100

    def test_circle_length(self):
        circle = Circle(10)
        assert circle.calculate_length() == self.PI * 20
