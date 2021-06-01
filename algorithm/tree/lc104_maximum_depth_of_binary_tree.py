# -*- coding: utf8 -*-

"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def max_depth_recursive(root: TreeNode) -> int:
    if root is None:
        return 0
    return 1 + max(max_depth_recursive(root.left), max_depth_recursive(root.right))


def max_depth_iterative(root: TreeNode) -> int:
    if root is None:
        return 0
    queue = [root]
    depth = 0
    while queue:
        depth += 1
        next_queue = []
        for node in queue:
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        queue = next_queue
    return depth


def test_max_depth():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert max_depth_recursive(root) == 3
    assert max_depth_iterative(root) == 3


if __name__ == '__main__':
    test_max_depth()
