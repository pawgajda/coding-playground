#!/use/vin/env python3
from redis_decorators import (
    RedisCaching,
    CacheElement,
    Cacheable,
    StringCacheable
)
import unittest


# connect to Redis' Docker Container
caching = RedisCaching('redis://localhost:6379')


# Cast int to str back and forth because Redis doesn't support int values
class CacheInt(CacheElement[int, str]):
    cacheable: Cacheable[str] = StringCacheable()

    def load(self, value: str) -> int:
        return int(value)

    def dump(self, value: int) -> str:
        return str(value)


# implement fibonacci with caching
@caching.cache_value(CacheInt())
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


class FibonacciTestCases(unittest.TestCase):
    def test_fibonacci(self):
        fib = fibonacci(10)
        expected = 55
        actual = fib

        self.assertEqual(expected, actual)

    def test_another_fibonacci(self):
        fib = fibonacci(15)
        expected = 610
        actual = fib

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
