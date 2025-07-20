#!/usr/bin/env python3
import unittest
from typing import Any


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value: Any, priority: int) -> None:
        # tuple: (value, priority)
        self.queue.append((value, priority))

    def dequeue(self) -> Any:
        # element: (value, priority)
        min_priority = 99
        min_index = -1

        for index, element in enumerate(self.queue):
            _, priority = element

            if priority < min_priority:
                min_priority = priority
                min_index = index

        value, priority = self.queue.pop(min_index)
        return value


class PriorityQueueTestCases(unittest.TestCase):
    def test_priority_enqueue(self):
        queue = PriorityQueue()

        queue.enqueue(10, 1)
        queue.enqueue(20, 2)
        queue.enqueue(30, 3)

        expected = (20, 2)
        actual = queue.queue[1]
        self.assertEqual(expected, actual)

    def test_priority_dequeue(self):
        queue = PriorityQueue()

        queue.queue = [
            (10, 10),
            (20, 5),
            (31, 7),
            (24, 3),
            (15, 1),
            (13, 1),
            (22, 2),
            (1, 1),
        ]

        queue_length = len(queue.queue)
        expected = [15, 13, 1, 22, 24, 20, 31, 10]
        actual = []

        for _ in range(queue_length):
            actual.append(queue.dequeue())

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
