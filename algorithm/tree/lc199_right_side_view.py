# -*- coding: utf8 -*-

"""
Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def right_side_view_BFS(root: TreeNode) -> List[int]:
    ret = []
    stack = [root]
    while stack:
        next_level = []
        node = None
        for node in stack:
            if node is None:
                continue
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        if node is not None:
            ret.append(node.val)
        stack = next_level
    return ret


def test_right_side_view():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    assert right_side_view_BFS(root) == [1, 3, 4]


if __name__ == '__main__':
    test_right_side_view()
