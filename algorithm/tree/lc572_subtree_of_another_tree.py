# -*- coding: utf8 -*-

"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure
and node values with a subtree of s.
A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def subtree_of_another_tree(s: TreeNode, t: TreeNode) -> bool:
    if not s:
        return False
    if is_same_tree(s, t):
        return True
    return subtree_of_another_tree(s.left, t) or subtree_of_another_tree(s.right, t)


def is_same_tree(s: TreeNode, t: TreeNode) -> bool:
    if not s and not t:
        return True
    if not s or not t:
        return False
    if s.val != t.val:
        return False
    return is_same_tree(s.left, t.left) and is_same_tree(s.right, t.right)


def test_subtree_of_another_tree():
    s_root = TreeNode(3)
    s_root.left = TreeNode(4)
    s_root.right = TreeNode(5)
    s_root.left.left = TreeNode(1)
    s_root.left.right = TreeNode(2)

    t_root = TreeNode(4)
    t_root.left = TreeNode(1)
    t_root.right = TreeNode(2)
    assert subtree_of_another_tree(s_root, t_root) is True


if __name__ == '__main__':
    test_subtree_of_another_tree()
