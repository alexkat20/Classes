import unittest
from Task4 import Palindrome


class TestNumbers(unittest.TestCase):
    def test_real_palindrome(self):
        palindrome = Palindrome(1234321)
        assert palindrome.check_for_palindrome()

    def test_not_palindrome(self):
        palindrome = Palindrome(1234)
        assert not palindrome.check_for_palindrome()

    def test_second_palindrome(self):
        palindrome = Palindrome(123321)
        assert palindrome.check_for_palindrome()
