#!/usr/bin/env python3
import unittest


def reverse_digits(number: int) -> int:
    rev = 0
    r = 0
    tmp = number

    while tmp > 0:
        r = tmp % 10
        rev = rev * 10 + r
        # decimal part of division operation
        tmp = tmp // 10

    return rev


class ReverseDigitsTests(unittest.TestCase):
    def test_reverse_digits(self):
        number = 456
        expected = 654

        actual = reverse_digits(number)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
