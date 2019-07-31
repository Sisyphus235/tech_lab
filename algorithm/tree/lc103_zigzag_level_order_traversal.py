# -*- coding: utf8 -*-

"""
Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def zigzag_level_order_traversal_recursive(root: TreeNode, ret, level):
    if root is None:
        return []
    if level > len(ret) - 1:
        ret.append([])
    if level & 1:
        ret[level].insert(0, root.val)
    else:
        ret[level].append(root.val)
    zigzag_level_order_traversal_recursive(root.left, ret, level + 1)
    zigzag_level_order_traversal_recursive(root.right, ret, level + 1)
    return ret


def zigzag_level_order_traversal_BFS(root: TreeNode) -> List[List[int]]:
    ret = []
    stack = [(root, 0, False)]
    while stack:
        root, level, is_visited = stack.pop()
        if root is None:
            continue
        if level > len(ret) - 1:
            ret.append([])
        if is_visited:
            if level & 1:
                ret[level].insert(0, root.val)
            else:
                ret[level].append(root.val)
        else:
            stack.append((root.right, level + 1, False))
            stack.append((root.left, level + 1, False))
            stack.append((root, level, True))
    return ret


def test_zigzag_level_order_traversal():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert zigzag_level_order_traversal_recursive(root, [], 0) == [[3], [20, 9], [15, 7]]

    assert zigzag_level_order_traversal_BFS(root) == [[3], [20, 9], [15, 7]]


if __name__ == '__main__':
    test_zigzag_level_order_traversal()
