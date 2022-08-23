"""
Write a function to find the maximum number without using max() function

"""


class MaxNumbers:
    def __init__(self, *args):
        self.numbers = args

    def find_maximum_number(self):
        num1 = 0
        for i in range(len(self)):
            if self[i] > num1:
                num1 = self[i]
        return num1


