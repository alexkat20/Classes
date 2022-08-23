import unittest
from Task1 import MaxNumbers


class TestMaxNumber(unittest.TestCase):
    def test_max_number(self):
        test_numbers = [1, 2, 3, 4, 5, 6]
        max_numbers = MaxNumbers(*test_numbers)
        self.assertEqual(max(test_numbers), max_numbers.find_maximum_number())
