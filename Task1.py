"""
Write a function to find the maximum number without using max() function

"""


class MaxNumbers:
    def __init__(self, *args):
        self.numbers = args

    def find_maximum_number(self):
        max1 = self.numbers[0]
        for x in self.numbers:
            if x > max1:
                max1 = x
        return max1



