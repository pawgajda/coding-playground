#!/usr/bin/env python3
from queue import PriorityQueue
from dataclasses import dataclass, field
from typing import Any
import unittest


@dataclass(order=True)
class PrioritizedItem:
    item: Any = field(compare=False)
    priority: int


class PriorityQueueTestCases(unittest.TestCase):
    def test_enqueue(self):
        queue = PriorityQueue()

        queue.put(PrioritizedItem(10, 1))
        queue.put(PrioritizedItem(20, 2))
        queue.put(PrioritizedItem(30, 3))

        expected = PrioritizedItem(20, 2)
        actual = queue.queue[1]

        print(queue.queue)
        self.assertEqual(expected, actual)

    def test_priority_dequeue(self):
        queue = PriorityQueue()

        queue.put(PrioritizedItem(10, 10))
        queue.put(PrioritizedItem(20, 5))
        queue.put(PrioritizedItem(31, 7))
        queue.put(PrioritizedItem(24, 3))
        queue.put(PrioritizedItem(15, 1))
        queue.put(PrioritizedItem(13, 1))
        queue.put(PrioritizedItem(22, 2))
        queue.put(PrioritizedItem(1, 1))

        queue_length = len(queue.queue)
        expected = [
            PrioritizedItem(15, 1),
            PrioritizedItem(13, 1),
            PrioritizedItem(1, 1),
            PrioritizedItem(22, 2),
            PrioritizedItem(24, 3),
            PrioritizedItem(20, 5),
            PrioritizedItem(31, 7),
            PrioritizedItem(10, 10)
        ]
        actual = []

        for _ in range(queue_length):
            actual.append(queue.get())

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
