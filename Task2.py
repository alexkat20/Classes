"""
Write a function to get identical numbers from two lists
"""


class IdenticalNumbers:
    def __init__(self, first_list, second_list):
        self.first_list = first_list
        self.second_list = second_list

    def get_identical_numbers(self):
        outputlist = []
        for item in self.first_list:
            if item in self.second_list and item not in outputlist:
                outputlist.append(item)
        return outputlist


