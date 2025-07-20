#!/usr/bin/env python3
from functools import cache, lru_cache
import unittest


@lru_cache(maxsize=None)
def fibonacci(a: int) -> int:
    if a < 2:
        return a
    else:
        return fibonacci(a - 1) + fibonacci(a - 2)


class FibonacciTestCases(unittest.TestCase):
    def test_fibonacci(self):
        expected = 55
        actual = fibonacci(10)
        self.assertEqual(expected, actual)


class FinonacciCacheTestCases(unittest.TestCase):
    def setUp(self):
        fibonacci.cache_clear()

    def test_fibonacci_single_hits(self):
        fibonacci(1)
        expected = 1
        actual = fibonacci.cache_info().misses
        self.assertEqual(expected, actual)

        expected = 0
        actual = fibonacci.cache_info().hits
        self.assertEqual(expected, actual)

    def test_fibonacci_cache(self):
        fibonacci(10)
        expected = 11
        actual = fibonacci.cache_info().misses
        self.assertEqual(expected, actual)

        expected = 8
        actual = fibonacci.cache_info().hits
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
