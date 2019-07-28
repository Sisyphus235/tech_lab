# -*- coding: utf8 -*-

"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,2,6,15,7],
      3
   /    \
  9     20
 / \   /  \
2  6  15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [2,6,15,7]
]
"""

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def level_order_traversal_recursive(root: TreeNode, ret, level):
    """
    add level to pre order recursion
    :param root:
    :param ret: return list
    :param level: current level in the given tree
    :return:
    """
    if root is None:
        return []
    if level > len(ret) - 1:
        ret.append([])
    ret[level].append(root.val)
    level_order_traversal_recursive(root.left, ret, level + 1)
    level_order_traversal_recursive(root.right, ret, level + 1)
    return ret


def level_order_traversal_BFS(root: TreeNode) -> List[List[int]]:
    ret = []
    stack = [(root, 0, False)]
    while stack:
        root, level, is_visited = stack.pop()
        if root is None:
            continue
        if level > len(ret) - 1:
            ret.append([])
        if is_visited:
            ret[level].append(root.val)
        else:
            stack.append((root.right, level + 1, False))
            stack.append((root.left, level + 1, False))
            stack.append((root, level, True))
    return ret


def test_level_order_traversal():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(6)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert level_order_traversal_recursive(root, [], 0) == [[3], [9, 20], [2, 6, 15, 7]]

    assert level_order_traversal_BFS(root) == [[3], [9, 20], [2, 6, 15, 7]]


if __name__ == '__main__':
    test_level_order_traversal()
