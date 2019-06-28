# -*- coding: utf8 -*-

"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


BUFFER = []


def pre_order_traversal_recursive(root: TreeNode):
    if root is not None:
        BUFFER.append(root.val)
        pre_order_traversal_recursive(root.left)
        pre_order_traversal_recursive(root.right)


def pre_order_traversal_iterative(root: TreeNode) -> List[int]:
    stack = []
    ret = []
    if root is not None:
        ret.append(root.val)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
        while stack:
            cur = stack.pop()
            ret.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
    return ret


def pre_order_traversal_iterative2(root: TreeNode) -> List[int]:
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
            stack.append((root.left, False))
            stack.append((root, True))
    return ret


def test_pre_order_traversal():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    pre_order_traversal_recursive(root)
    assert BUFFER == [1, 2, 3]

    assert pre_order_traversal_iterative(root) == [1, 2, 3]
    assert pre_order_traversal_iterative2(root) == [1, 2, 3]


if __name__ == '__main__':
    """
    技巧：一个栈存放待处理的树节点，如果子树存在则按照遍历相反顺序入栈，前序是节点、左、右，所以入栈顺序是右子树、左子树，节点
    """
    test_pre_order_traversal()
