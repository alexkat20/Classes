import unittest
from Task5 import LongestString


class TestNumbers(unittest.TestCase):
    def test_first_longest_string(self):
        strings = LongestString(["cat", "car", "fear", "center"])
        assert strings.get_the_longest_string() == "center"

    def test_second_longest_string(self):
        strings = LongestString(["cat", "dog", "shatter", "donut", "at", "todo", ""])
        assert strings.get_the_longest_string() == "shatter"
