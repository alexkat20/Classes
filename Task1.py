"""
Write a function to find the maximum number without using max() function

"""


class MaxNumbers:
    def __init__(self, *args):
        self.numbers = args

    def find_maximum_number(self):
        num1 = 0
        for i in range(len(self.numbers)):
            if self.numbers[i] > num1:
                num1 = self.numbers[i]
        return num1


