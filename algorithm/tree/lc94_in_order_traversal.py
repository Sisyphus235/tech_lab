# -*- coding: utf8 -*-

"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
"""

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


BUFFER = []


def in_order_traversal_recursive(root: TreeNode):
    if root is not None:
        in_order_traversal_recursive(root.left)
        BUFFER.append(root.val)
        in_order_traversal_recursive(root.right)


def in_order_traversal_iterative(root: TreeNode) -> List[int]:
    ret = []
    stack = [(root, False)]
    while stack:
        root, is_visited = stack.pop()
        if root is None:
            continue
        if is_visited:
            ret.append(root.val)
        else:
            stack.append((root.right, False))
            stack.append((root, True))
            stack.append((root.left, False))

    return ret


def test_in_order_traversal():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    in_order_traversal_recursive(root)
    assert BUFFER == [1, 3, 2]

    assert in_order_traversal_iterative(root) == [1, 3, 2]


if __name__ == '__main__':
    test_in_order_traversal()
