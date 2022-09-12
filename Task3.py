"""
Write functions for the perimeter and square of a rectangle and functions for the square and length of a circle
"""


class Rectangle:
    def __init__(self, first_side, second_side):
        self.first_side, self.second_side = first_side, second_side

    def calculate_perimeter(self):
        perimeter = 2 * (self.first_side+self.second_side)
        return perimeter



    def calculate_square(self):
        area = (self.first_side) * (self.second_side)
        return area



class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_length(self):
        length =(self.radius * 3.14) * 2
        return length

    def calculate_square(self):
        area = (3.14) * (self.radius)**2
        return area
