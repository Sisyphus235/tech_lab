# -*- coding: utf8 -*-

"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


BUFFER = []


def post_order_traversal_recursive(root: TreeNode):
    if root is not None:
        post_order_traversal_recursive(root.left)
        post_order_traversal_recursive(root.right)
        BUFFER.append(root.val)


def post_order_traversal_iterative(root: TreeNode) -> List[int]:
    ret = []
    stack = [(root, False)]
    while stack:
        root, is_visited = stack.pop()
        if root is None:
            continue
        if is_visited:
            ret.append(root.val)
        else:
            stack.append((root, True))
            stack.append((root.right, False))
            stack.append((root.left, False))
    return ret


def test_post_order_traversal():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    post_order_traversal_recursive(root)
    assert BUFFER == [3, 2, 1]

    assert post_order_traversal_iterative(root) == [3, 2, 1]


if __name__ == '__main__':
    test_post_order_traversal()
