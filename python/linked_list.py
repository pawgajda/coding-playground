#!/usr/bin/env python3
from __future__ import annotations
from typing import Any, TYPE_CHECKING
import dataclasses
import unittest


class Node:
    if TYPE_CHECKING:
        value: Any
        next: Node | None

    def __init__(self, value: Any):
        self.value = value
        self.next = None


class LinkedList:
    if TYPE_CHECKING:
        head: Node | None

    def __init__(self):
        self.head = None

    def insert(self, value: Any, pos: int | None = None) -> None:
        node = Node(value)

        if self.head is None:
            self.head = node
            return

        current = self.head
        current_pos = 0

        while current.next:
            if pos is not None and current_pos == pos - 1:
                break

            current = current.next
            current_pos += 1

        if pos is not None and pos > current_pos + 1:
            raise IndexOutOfRangeException(pos, current_pos)
        elif pos is not None:
            node.next = current.next

        current.next = node

    def get(self, pos: int) -> Any:
        current = self.head
        current_pos = 0

        if current is None:
            raise IndexOutOfRangeException(pos, current_pos)

        while current.next:
            if current_pos == pos:
                return current.value

            current = current.next
            current_pos += 1

        if pos > current_pos + 1:
            raise IndexOutOfRangeException(pos, current_pos)

        return current.value

    def traversal(self) -> None:
        current = self.head
        current_pos = 0

        while current.next:
            print(current_pos, current.value)
            current = current.next
            current_pos += 1

    def delete(self, pos: int) -> None:
        current = self.head
        current_pos = 0

        if current is None:
            raise IndexOutOfRangeException(pos, current_pos)

        if pos == 0:
            self.head = current.next

        while current.next:
            if current_pos == pos - 1:
                node = current.next
                current.next = node.next

            current = current.next
            current_pos += 1

        if pos > current_pos:
            raise IndexOutOfRangeException(pos, current_pos)


@dataclasses.dataclass(frozen=True)
class IndexOutOfRangeException(Exception):
    index: int
    range_size: int


class LinkedListTests(unittest.TestCase):
    def test_insert_at_middle_pos(self):
        test_list = LinkedList()
        test_list.insert("a")
        test_list.insert("b")
        test_list.insert("c")
        # insert at pos 1
        test_list.insert("d", 1)

        expected = "d"
        actual = test_list.head.next.value

        self.assertEqual(expected, actual)

    def test_insert_out_of_bounds(self):
        test_list = LinkedList()
        test_list.insert("a")
        test_list.insert("b")

        with self.assertRaises(IndexOutOfRangeException) as e:
            test_list.insert("c", 5)

    def test_get_last_element(self):
        test_list = LinkedList()
        test_list.head = Node(420)
        test_list.head.next = Node(69)
        test_list.head.next.next = Node(2137)

        expected = 2137
        actual = test_list.get(2)

        self.assertEqual(expected, actual)

    def test_get_first_element(self):
        test_list = LinkedList()
        test_list.head = Node(69)

        expected = 69
        actual = test_list.get(0)

        self.assertEqual(expected, actual)

    def test_get_middle_element(self):
        test_list = LinkedList()
        test_list.head = Node(69)
        test_list.head.next = Node(420)
        test_list.head.next.next = Node(1337)
        test_list.head.next.next.next = Node(2137)

        expected = 420
        actual = test_list.get(1)

        self.assertEqual(expected, actual)

    def test_get_empty(self):
        test_list = LinkedList()

        with self.assertRaises(IndexOutOfRangeException) as e:
            test_list.get(0)

    def test_get_out_of_range(self):
        test_list = LinkedList()
        test_list.head = Node("a")
        test_list.head.next = Node("b")
        test_list.head.next.next = Node("c")

        with self.assertRaises(IndexOutOfRangeException) as e:
            test_list.get(5)

    def test_delete_middle(self):
        test_list = LinkedList()
        test_list.head = Node("a")
        test_list.head.next = Node("b")
        test_list.head.next.next = Node("c")
        test_list.head.next.next.next = Node("d")

        test_list.delete(1)
        expected = "c"
        actual = test_list.head.next.value

        self.assertEqual(expected, actual)

    def test_delete_first_element(self):
        test_list = LinkedList()
        test_list.head = Node("a")
        test_list.head.next = Node("b")
        test_list.head.next.next = Node("c")

        test_list.delete(0)

        expected = "b"
        actual = test_list.head.value

        self.assertEqual(expected, actual)

    def test_delete_lonely_element(self):
        test_list = LinkedList()
        test_list.head = Node("a")

        test_list.delete(0)

        expected = None
        actual = test_list.head

        self.assertEqual(expected, actual)

    def test_delete_out_of_range(self):
        test_list = LinkedList()
        test_list.head = Node("a")
        test_list.head.next = Node("b")

        with self.assertRaises(IndexOutOfRangeException) as e:
            test_list.delete(2)

    def test_delete_empty_list(self):
        test_list = LinkedList()

        with self.assertRaises(IndexOutOfRangeException) as e:
            test_list.delete(0)


if __name__ == "__main__":
    unittest.main()
