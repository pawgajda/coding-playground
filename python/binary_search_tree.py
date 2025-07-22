#!/usr/bin/env python3
from __future__ import annotations
from typing import TYPE_CHECKING
from dataclasses import dataclass
import unittest


class Node:
    if TYPE_CHECKING:
        value: int
        left: Node | None
        right: Node | None

    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def get_successor_recursive(self) -> Node | None:
        current_node = self.right

        while current_node and current_node.left:
            current_node = current_node.left

        return current_node

    def delete_recursive(self, value: int) -> Node | None:
        # when root is None
        if self is None:
            return self

        # searching in a subtree
        if self.value < value:
            self.right = self.right.delete_recursive(value)
        elif self.value > value:
            self.left = self.left.delete_recursive(value)
        # when found
        else:
            if not self.left:
                return self.right
            elif not self.right:
                return self.left
            else:
                successor = self.get_successor_recursive()
                self.value = successor.value
                self.right = self.right.delete_recursive(successor.value)

        return self


class BinarySearchTree:
    if TYPE_CHECKING:
        root: Node | None

    def __init__(self):
        self.root = None

    def insert(self, value: int) -> None:
        node = Node(value)

        if self.root is None:
            self.root = node
            return

        current_node = self.root

        while current_node:
            add_left = False
            add_right = False

            if current_node.value == value:
                raise ValueAlreadyExistException(value)

            previous_node = current_node

            if current_node.value > value:
                current_node = current_node.left
                add_left = True
            elif current_node.value < value:
                current_node = current_node.right
                add_right = True

        if add_left is True:
            previous_node.left = node

        if add_right is True:
            previous_node.right = node

    def delete(self, value: int) -> None:
        self.root.delete_recursive(value)


@dataclass(frozen=True)
class ValueAlreadyExistException(Exception):
    value: int


class BinarySearchTreeTests(unittest.TestCase):
    def test_insert_root(self):
        tree = BinarySearchTree()
        tree.insert(1)

        expected = 1
        actual = tree.root.value

        self.assertEqual(expected, actual)

    def test_insert_item(self):
        tree = BinarySearchTree()
        tree.root = Node(100)

        tree.root.left = Node(20)
        tree.root.right = Node(500)

        tree.root.left.left = Node(10)
        tree.root.left.right = Node(30)

        tree.insert(2137)

        expected = 2137
        actual = tree.root.right.right.value

        self.assertEqual(expected, actual)

    def test_insert_existing(self):
        tree = BinarySearchTree()
        tree.root = Node(100)

        tree.root.left = Node(20)
        tree.root.right = Node(500)

        tree.root.left.left = Node(10)
        tree.root.left.right = Node(30)

        with self.assertRaises(ValueAlreadyExistException) as e:
            tree.insert(500)

    def test_insert_last(self):
        tree = BinarySearchTree()
        tree.root = Node(100)

        tree.root.left = Node(20)
        tree.root.right = Node(500)

        tree.root.left.left = Node(10)
        tree.root.left.right = Node(30)

        tree.insert(2137)

        expected = 2137
        actual = tree.root.right.right.value
        self.assertEqual(expected, actual)

    def test_delete_item(self):
        tree = BinarySearchTree()
        tree.root = Node(100)

        tree.root.left = Node(20)
        tree.root.right = Node(500)

        tree.root.left.left = Node(10)
        tree.root.left.right = Node(30)

        tree.delete(20)

        expected = 30
        actual = tree.root.left.value

        self.assertEqual(expected, actual)

        expected_successor = None
        actual_successor = tree.root.left.right
        self.assertEqual(expected_successor, actual_successor)

        expected_child = 10
        actual_child = tree.root.left.left.value
        self.assertEqual(expected_child, actual_child)

    def test_delete_item_big(self):
        tree = BinarySearchTree()

        # root
        tree.root = Node(50)
        # level 1
        tree.root.left = Node(30)
        tree.root.right = Node(70)
        # level 2
        tree.root.left.left = Node(20)
        tree.root.left.right = Node(40)

        tree.root.right.left = Node(60)
        tree.root.right.right = Node(80)
        # level 3
        tree.root.left.left.left = Node(15)
        tree.root.left.left.right = Node(25)

        tree.root.left.right.left = Node(35)
        tree.root.left.right.right = Node(45)

        tree.root.right.left.left = Node(47)
        tree.root.right.left.right = Node(65)

        tree.root.right.right.left = Node(75)
        tree.root.right.right.right = Node(85)
        # level 4
        tree.root.left.left.left.left = Node(10)
        tree.root.left.left.left.right = Node(18)

        tree.root.left.left.right.left = Node(22)
        tree.root.left.left.right.right = Node(28)

        tree.root.left.right.left.left = Node(32)
        tree.root.left.right.left.right = Node(38)

        tree.root.left.right.right.left = Node(42)
        tree.root.left.right.right.right = Node(48)

        tree.root.right.left.left.left = Node(44)
        tree.root.right.left.left.right = Node(49)

        tree.root.right.left.right.left = Node(62)
        tree.root.right.left.right.right = Node(68)

        tree.root.right.right.left.left = Node(72)
        tree.root.right.right.left.right = Node(78)

        tree.root.right.right.right.left = Node(82)
        tree.root.right.right.right.right = Node(90)

        tree.delete(30)

        expected = 32
        actual = tree.root.left.value
        self.assertEqual(expected, actual)

        expected_successor = None
        actual_successor = tree.root.left.right.left.left
        self.assertEqual(expected_successor, actual_successor)

        expected_child = 38
        actual_child = tree.root.left.right.left.right.value
        self.assertEqual(expected_child, actual_child)

    def test_delete_last_item(self):
        tree = BinarySearchTree()
        tree.root = Node(100)

        tree.root.left = Node(20)
        tree.root.right = Node(500)

        tree.root.left.left = Node(10)
        tree.root.left.right = Node(30)

        tree.delete(30)

        expected = None
        actual = tree.root.left.right

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
