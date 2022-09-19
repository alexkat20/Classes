"""
Write a Python program find the longest string of a given list of strings
"""


class LongestString:
    def __init__(self, list_with_strings):
        self.list_with_strings = list_with_strings

    def get_the_longest_string(self):
        return  max(self.list_with_strings, key=len)
