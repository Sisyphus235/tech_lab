# -*- coding: utf8 -*-

"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_same_tree_recursive(p: TreeNode, q: TreeNode) -> bool:
    if p is None and q is None:
        return True
    if p is not None and q is not None:
        return p.val == q.val and is_same_tree_recursive(p.left, q.left) and is_same_tree_recursive(p.right, q.right)
    return False


def is_same_tree_iterative(p: TreeNode, q: TreeNode) -> bool:
    stack1, stack2 = [p], [q]
    while stack1 and stack2:
        s1, s2 = stack1.pop(), stack2.pop()
        if s1 is None and s2 is None:
            continue
        if s1 is not None and s2 is not None:
            if s1.val != s2.val:
                return False
            stack1.append(s1.right)
            stack2.append(s2.right)
            stack1.append(s1.left)
            stack2.append(s2.left)
        else:
            return False
    return len(stack1) == len(stack2) == 0


def test_is_same_tree():
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    assert is_same_tree_recursive(p, q) is True
    assert is_same_tree_iterative(p, q) is True

    p = TreeNode(1)
    p.left = TreeNode(2)
    q = TreeNode(1)
    q.right = TreeNode(2)
    assert is_same_tree_recursive(p, q) is False
    assert is_same_tree_iterative(p, q) is False


if __name__ == '__main__':
    test_is_same_tree()
