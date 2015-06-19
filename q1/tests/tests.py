__author__ = 'bj'

import unittest
from q1 import find_longest_inc_subsequence as fls


class TestFindLongestIncrementingSubSequence(unittest.TestCase):

    def test_example_one(self):
        self.assertEqual(fls([1, 4, 1, 4, 2, 1, 3, 5, 6, 2, 3, 7]), 4)

    def test_example_two(self):
        self.assertEqual(fls([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), 3)

    def test_example_three(self):
        self.assertEqual(fls([2, 7, 1, 8, 2, 8, 1]), 2)

    def test_empty_list(self):
        self.assertEqual(fls([]), 0)

    def test_single_value(self):
        self.assertEqual(fls([7]), 0)

    def test_all_same_value(self):
        self.assertEqual(fls([2, 2, 2, 2, 2, 2, 2]), 0)

    def test_a_string(self):
        self.assertEqual(fls(['abc']), 0)

    def test_list_of_strings(self):
        self.assertEqual(fls(['a', 'b', 'c', 'b']), 3)

    def text_speed(self):
        pass

if __name__ == '__main__':
    unittest.main()
