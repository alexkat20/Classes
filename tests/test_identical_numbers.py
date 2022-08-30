import unittest
from Task2 import IdenticalNumbers


class TestIdenticalNumbers(unittest.TestCase):
    def test_max_number(self):
        test_first_list = [1, 2, 3, 4, 5, 6]
        test_second_list = [4, 5, 6, 7, 8, 9]

        numbers = IdenticalNumbers(test_first_list, test_second_list)

        self.assertEqual(numbers.get_identical_numbers(), [4, 5, 6])
