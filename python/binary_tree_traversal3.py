#!/usr/bin/env python3
from __future__ import annotations
from typing import Any, TYPE_CHECKING
import unittest


class TraversalMethod(Enum):
    PRE_ORDER = 1
    IN_ORDER = 2
    POST_ORDER = 3


class Node:
    if TYPE_CHECKING:
        value: Any
        left: Node | None
        right: Node | None

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    if TYPE_CHECKING:
        root: Node | None

    def __init__(self):
        self.root = None

    def bredth_first_search(self) -> list[Any]:
        lst = []

        if self.root:
            queue = [self.root]

            while queue:
                for _ in queue:
                    node = queue.pop(0)
                    lst.append(node.value)

                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)

        return lst


class BinaryTreeTests(unittest.TestCase):
    # Breadth First Search
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

    def test_traverse_breadth_first_search(self):
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

        expected = [11, 10, 8, 5, 9, 2, 6, 3, 1, 4, 7]
        actual = tree.bredth_first_search()

        self.assertEqual(expected, actual)

    def test_traverse_breadth_empty(self):
        tree = BinaryTree()

        expected = []
        actual = tree.bredth_first_search()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
