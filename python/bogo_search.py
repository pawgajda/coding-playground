#!/usr/bin/env python3
import random
import unittest


def bogo_search(
    arr: list,
    n: int,
    rand: random.Random | None = None,
    max_tries: int = 9999
) -> tuple[int, int]:

    if rand is None:
        rand = random.Random()

    tries = 0

    # handle empty list
    if len(arr) == 0:
        return (-1, tries)

    while tries < max_tries:
        index = rand.randrange(0, len(arr))
        tries += 1

        if arr[index] == n:
            return (index, tries)

    return (-1, tries)


class BogoSearchTests(unittest.TestCase):
    random_seed = 749

    def test_bogo_search(self):
        rand = random.Random(self.random_seed)
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

        expected = 9  # index of 10
        actual, tries = bogo_search(lst, 10, rand)
        print(f"Test Bogo Search Tries: {tries}")
        self.assertEqual(expected, actual)

    def test_failure(self):
        rand = random.Random(self.random_seed)
        lst = [9, 1, 3, 5, 2, 7, 4, 8, 6]

        expected = -1  # expected failure
        actual, tries = bogo_search(lst, 10, rand)
        print(f"Test Failure Tries {tries}")
        self.assertEqual(expected, actual)

    def test_search_empty(self):
        rand = random.Random(self.random_seed)
        lst = []

        expected = -1  # expected failure
        actual, tries = bogo_search(lst, 10, rand)
        print(f"Test Search Empty Tries {tries}")
        self.assertEqual(expected, actual)

    def test_huge_list(self):
        rand = random.Random(self.random_seed)
        lst = [i for i in range(1, 1025)]

        expected = 419  # index of 420
        actual, tries = bogo_search(lst, 420, rand)
        print(f"Test Search Huge List Tries {tries}")
        self.assertEqual(expected, actual)

    def test_random_list(self):
        rand = random.Random(self.random_seed)
        lst = rand.sample(range(1, 257), 256)

        expected = 133
        actual, tries = bogo_search(lst, 53, rand)
        print(f"Test Random List Tries: {tries}")
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
