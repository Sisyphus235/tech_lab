# -*- coding: utf8 -*-

"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_balanced_recursive1(root: TreeNode) -> bool:
    if root is None:
        return True
    left = get_depth(root.left)
    right = get_depth(root.right)
    if abs(left - right) > 1:
        return False
    return is_balanced_recursive1(root.left) and is_balanced_recursive1(root.right)


def get_depth(node: TreeNode) -> int:
    if node is None:
        return 0
    return 1 + max(get_depth(node.left), get_depth(node.right))


def is_balanced_recursive2(root: TreeNode) -> bool:
    if check_depth(root) == -1:
        return False
    return True


def check_depth(node: TreeNode) -> int:
    if node is None:
        return 0
    left = check_depth(node.left)
    if left == -1:
        return -1
    right = check_depth(node.right)
    if right == -1:
        return -1
    if abs(left - right) > 1:
        return -1
    else:
        return 1 + max(left, right)


def test_is_balanced():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert is_balanced_recursive1(root) is True
    assert is_balanced_recursive2(root) is True

    root = TreeNode(1)
    assert is_balanced_recursive1(root) is True
    assert is_balanced_recursive2(root) is True

    root = TreeNode(1)
    root.right = TreeNode(2)
    assert is_balanced_recursive1(root) is True
    assert is_balanced_recursive2(root) is True

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    assert is_balanced_recursive1(root) is False
    assert is_balanced_recursive2(root) is False


if __name__ == '__main__':
    test_is_balanced()
