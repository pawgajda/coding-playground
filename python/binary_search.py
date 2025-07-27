#!/usr/bin/env python3
import unittest


# iterative implementation of binary search
def binary_search(arr, low, high, n):
    # base case
    while low <= high:

        # calculate middle index of the list
        mid = low + (high - low) // 2

        # instant find
        if arr[mid] == n:
            return mid
        # if n is greater, ignore lower half
        elif arr[mid] < n:
            low = mid + 1
        # else if n is smaller, ignore higher half
        else:
            high = mid - 1

    # not found
    return -1


class BinarySearchTests(unittest.TestCase):
    def test_search_found(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

        expected = 11  # 12 at index arr[11]
        actual = binary_search(arr, 0, len(arr) - 1, 12)
        self.assertEqual(expected, actual)

    def test_search_not_found(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

        expected = -1.  # function returns -1 when element was not found
        actual = binary_search(arr, 0, len(arr) - 1, 1337)
        self.assertEqual(expected, actual)

    def test_search_empty(self):
        arr = []

        expected = -1
        actual = binary_search(arr, 0, len(arr) - 1, 8)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
