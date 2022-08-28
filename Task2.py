"""
Write a function to get identical numbers from two lists
"""


class IdenticalNumbers:
    def __init__(self, first_list, second_list):
        self.first_list = first_list
        self.second_list = second_list

    def get_identical_numbers(self):
        a = []
        for i in range(len(self.first_list)):
            if self.first_list[i] in self.second_list:
                a.append(self.first_list[i])
        return a


