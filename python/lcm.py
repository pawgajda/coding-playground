#!/usr/bin/env python3

import unittest
from gcd import gcd


# Least Common Multiple using GCD
def lcm(a: int, b: int) -> int:
    result = abs(a) * abs(b) / gcd(a, b)
    return result


class TestLcm(unittest.TestCase):
    def test_lcm(self):
        expected = 42
        actual = lcm(21, 6)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
