# -*- coding: utf8 -*-

"""
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1

Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7

Note: You may assume the tree (i.e., the given root node) is not NULL.
"""

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def find_bottom_left_tree_value(root: TreeNode) -> int:
    ret = None
    stack = [root]
    while stack:
        next_stack = []
        cur = 0
        ret = stack[cur].val
        while cur < len(stack):
            if stack[cur] is None:
                continue
            if stack[cur].left is not None:
                next_stack.append(stack[cur].left)
            if stack[cur].right is not None:
                next_stack.append(stack[cur].right)
            cur += 1
        stack = next_stack
    return ret


def test_find_bottom_left_tree_value():
    root = TreeNode(1)
    assert find_bottom_left_tree_value(root) == 1

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    assert find_bottom_left_tree_value(root) == 1

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    assert find_bottom_left_tree_value(root) == 7


if __name__ == '__main__':
    test_find_bottom_left_tree_value()
