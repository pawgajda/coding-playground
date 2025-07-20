#!/usr/bin/env python3
from functools import lru_cache
import unittest


@lru_cache(maxsize=None)
def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


class FactorialTestCases(unittest.TestCase):
    def test_factorial(self):
        expected = 120
        actual = factorial(5)
        self.assertEqual(expected, actual)


class FactorialCacheTestCases(unittest.TestCase):
    def setUp(self):
        factorial.cache_clear()

    def test_factorial_cache(self):
        factorial(5)
        expected = 6
        actual = factorial.cache_info().misses
        self.assertEqual(expected, actual)

        expected = 0
        actual = factorial.cache_info().hits
        self.assertEqual(expected, actual)

        factorial(5)
        expected = 1
        actual = factorial.cache_info().hits
        self.assertEqual(expected, actual)

        factorial(10)
        expected = 11
        actual = factorial.cache_info().misses
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
