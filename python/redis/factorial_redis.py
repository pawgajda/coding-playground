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


# implement factorial with caching
@caching.cache_value(CacheInt())
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

    def test_another_factorial(self):
        expected = 720
        actual = factorial(6)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
