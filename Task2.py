"""
Write a function to get identical numbers from two lists
"""


class IdenticalNumbers:
    def __init__(self, first_list, second_list):
        self.first_list = first_list
        self.second_list = second_list

    def get_identical_numbers(self):
        identical_numbers = []
        for n in self.first_list:
            if n in self.second_list:
                identical_numbers.append(n)
        return identical_numbers




