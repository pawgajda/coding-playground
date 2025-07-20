#!/usr/bin/env python3
from __future__ import annotations
from typing import Any, TYPE_CHECKING
import unittest


class Node:
    if TYPE_CHECKING:
        value: Any
        left: Node | None
        right: Node | None

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def pre_order_traversal(self) -> list[Any]:
        lst = [self.value]

        if self.left:
            lst += self.left.pre_order_traversal()

        if self.right:
            lst += self.right.pre_order_traversal()

        return lst

    def in_order_traversal(self) -> list[Any]:
        lst = []

        if self.left:
            lst += self.left.in_order_traversal()

        lst.append(self.value)

        if self.right:
            lst += self.right.in_order_traversal()

        return lst

    def post_order_traversal(self) -> list[Any]:
        lst = []

        if self.left:
            lst += self.left.post_order_traversal()

        if self.right:
            lst += self.right.post_order_traversal()

        lst.append(self.value)
        return lst

    def invert(self) -> Node:
        self.left, self.right = self.right, self.left

        if self.left:
            self.left = self.left.invert()

        if self.right:
            self.right = self.right.invert()

        return self


class BinaryTree:
    if TYPE_CHECKING:
        root: Node | None

    def __init__(self):
        self.root = None

    def pre_order_traversal(self) -> list[Any]:
        lst = []
        if self.root:
            lst = self.root.pre_order_traversal()
        return lst

    def in_order_traversal(self) -> list[Any]:
        lst = []
        if self.root:
            lst = self.root.in_order_traversal()
        return lst

    def post_order_traversal(self) -> list[Any]:
        lst = []
        if self.root:
            lst = self.root.post_order_traversal()
        return lst

    def invert(self) -> BinaryTree:
        tree = BinaryTree()

        if self.root is None:
            return tree

        tree.root = self.root.invert()
        return tree


class BinaryTreeTests(unittest.TestCase):
    # Traversal (In, Pre, Post Order):
    #
    #                    11
    #                   /  \
    #                  /    \
    #                 /      \
    #                10      8
    #               /  \    /  \
    #              /    \  /    \
    #             5      9 2     6
    #            / \    / \
    #           /   \  /   \
    #          3     1 4    7

    def test_traverse_pre_order(self):
        tree = BinaryTree()
        # root
        tree.root = Node(11)
        # root's leaves
        tree.root.left = Node(10)
        tree.root.right = Node(8)
        # 10's leaves
        tree.root.left.left = Node(5)
        tree.root.left.right = Node(9)
        # 5's leaves
        tree.root.left.left.left = Node(3)
        tree.root.left.left.right = Node(1)
        # 9's leaves
        tree.root.left.right.left = Node(4)
        tree.root.left.right.right = Node(7)
        # 8's leaves
        tree.root.right.left = Node(2)
        tree.root.right.right = Node(6)

        expected = [11, 10, 5, 3, 1, 9, 4, 7, 8, 2, 6]
        actual = tree.pre_order_traversal()

        self.assertEqual(expected, actual)

    def test_traverse_in_order(self):
        tree = BinaryTree()
        # root
        tree.root = Node(11)
        # root's leaves
        tree.root.left = Node(10)
        tree.root.right = Node(8)
        # 10's leaves
        tree.root.left.left = Node(5)
        tree.root.left.right = Node(9)
        # 5's leaves
        tree.root.left.left.left = Node(3)
        tree.root.left.left.right = Node(1)
        # 9's leaves
        tree.root.left.right.left = Node(4)
        tree.root.left.right.right = Node(7)
        # 8's leaves
        tree.root.right.left = Node(2)
        tree.root.right.right = Node(6)

        expected = [3, 5, 1, 10, 4, 9, 7, 11, 2, 8, 6]
        actual = tree.in_order_traversal()

        self.assertEqual(expected, actual)

    def test_traverse_post_order(self):
        tree = BinaryTree()
        # root
        tree.root = Node(11)
        # root's leaves
        tree.root.left = Node(10)
        tree.root.right = Node(8)
        # 10's leaves
        tree.root.left.left = Node(5)
        tree.root.left.right = Node(9)
        # 5's leaves
        tree.root.left.left.left = Node(3)
        tree.root.left.left.right = Node(1)
        # 9's leaves
        tree.root.left.right.left = Node(4)
        tree.root.left.right.right = Node(7)
        # 8's leaves
        tree.root.right.left = Node(2)
        tree.root.right.right = Node(6)

        expected = [3, 1, 5, 4, 7, 9, 10, 2, 6, 8, 11]
        actual = tree.post_order_traversal()

        self.assertEqual(expected, actual)

    def test_traverse_empty_pre_order(self):
        tree = BinaryTree()

        expected = []
        actual = tree.pre_order_traversal()

        self.assertEqual(expected, actual)

    def test_traverse_empty_in_order(self):
        tree = BinaryTree()

        expected = []
        actual = tree.in_order_traversal()

        self.assertEqual(expected, actual)

    def test_traverse_empty_post_order(self):
        tree = BinaryTree()

        expected = []
        actual = tree.post_order_traversal()

        self.assertEqual(expected, actual)

    # original:
    #                    11
    #                   /  \
    #                  /    \
    #                 /      \
    #                10      8
    #               /  \    /  \
    #              /    \  /    \
    #             5      9 2     6
    # inverted:
    #                    11
    #                   /  \
    #                  /    \
    #                 /      \
    #                8       10
    #               /  \    /  \
    #              /    \  /    \
    #             6      2 9     5

    def test_invert_tree(self):
        tree = BinaryTree()
        # root
        tree.root = Node(11)
        # root's leaves
        tree.root.left = Node(10)
        tree.root.right = Node(8)
        # 10's leaves
        tree.root.left.left = Node(5)
        tree.root.left.right = Node(9)
        # 8's leaves
        tree.root.right.left = Node(2)
        tree.root.right.right = Node(6)

        new_tree = tree.invert()

        self.assertEqual(11, new_tree.root.value)

        self.assertEqual(10, new_tree.root.right.value)
        self.assertEqual(8, new_tree.root.left.value)

        self.assertEqual(5, new_tree.root.right.right.value)
        self.assertEqual(9, new_tree.root.right.left.value)

        self.assertEqual(2, new_tree.root.left.right.value)
        self.assertEqual(6, new_tree.root.left.left.value)


if __name__ == "__main__":
    unittest.main()
