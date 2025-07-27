#!/usr/bin/env python3
import unittest


def linear_search(arr, n):
    i = 0

    while i < len(arr):
        if arr[i] == n:
            return i
        i += 1

    # not found
    return -1


class BinarySearchTests(unittest.TestCase):
    def test_search_found(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

        expected = 11  # 12 at index arr[11]
        actual = linear_search(arr, 12)
        self.assertEqual(expected, actual)

    def test_search_not_found(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

        expected = -1.  # function returns -1 when element was not found
        actual = linear_search(arr, 1337)
        self.assertEqual(expected, actual)

    def test_search_empty(self):
        arr = []

        expected = -1
        actual = linear_search(arr, 8)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
