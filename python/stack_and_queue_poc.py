#!/usr/bin/env python3
import unittest


class StackTestCases(unittest.TestCase):
    def test_push(self):
        stack = [10, 16, 8, 6, 4, 2]
        # push 1 on top of the stack
        stack.append(1)

        expected = 1
        actual = stack[-1]

        self.assertEqual(expected, actual)

    def test_pop(self):
        stack = [10, 16, 8, 6, 4, 2, 0, 1]

        expected = 1
        # pop last element of the stack
        actual = stack.pop()

        self.assertEqual(expected, actual)

    def test_peek(self):
        stack = [10, 16, 8, 4, 2, 0, 1, 9]

        expected = 9
        actual = stack[-1]

        self.assertEqual(expected, actual)


class QueueTestCases(unittest.TestCase):
    def test_enqueue(self):
        queue = [1, 2, 3, 4, 5]

        # enqueue
        queue.append(7)

        expected = 7
        actual = queue[-1]

        self.assertEqual(expected, actual)

    def test_dequeue(self):
        queue = [1, 2, 3, 4, 5]

        expected = 1
        # dequeue
        actual = queue.pop(0)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
