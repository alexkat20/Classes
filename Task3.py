"""
Write functions for the perimeter and square of a rectangle and functions for the square and length of a circle
"""


class Rectangle:
    def __init__(self, first_side, second_side):
        self.first_side, self.second_side = first_side, second_side

    def calculate_perimeter(self):
        return self.first_side*2 + self.second_side*2

    def calculate_square(self):
        return self.first_side*self.second_side


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_length(self):
        return self.radius*2*3.14

    def calculate_square(self):
        return 3.14*self.radius*self.radius
