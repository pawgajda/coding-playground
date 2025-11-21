#!/usr/bin/env python3
import unittest


# Greatest Common Divisor
def gcd(a: int, b: int) -> int:
    # keep looking for GCD until remainder of a / b equals 0
    while b != 0:
        # calculate the remainder of a / b
        r = a % b
        # swap values
        a = b
        b = r
    return a


class GcdTests(unittest.TestCase):
    def test_gcd(self):
        expected = 8
        actual = gcd(56, 48)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
