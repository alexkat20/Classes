"""
Write a Python program to check whether the given strings are palindromes or not. Return True, False
"""


class Palindrome:
    def __init__(self, number):
        self.number = number

    def check_for_palindrome(self):
        return str(self.number) == str(self.number)[::-1]









