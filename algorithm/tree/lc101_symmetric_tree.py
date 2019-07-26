# -*- coding: utf8 -*-

"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3

Note:
Bonus points if you could solve it both recursively and iteratively.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_symmetric_tree_recursive(root: TreeNode) -> bool:
    if root is None:
        return True
    return is_symmetric(root.left, root.right)


def is_symmetric(left: TreeNode, right: TreeNode) -> bool:
    if left is None and right is None:
        return True
    if left is None or right is None or left.val != right.val:
        return False
    return is_symmetric(left.left, right.right) and is_symmetric(left.right, right.left)


def is_symmetric_tree_iterative(root: TreeNode) -> bool:
    queue = [root]
    while queue:
        next_queue = []
        level_num = []
        for node in queue:
            if node is None:
                level_num.append(None)
            else:
                next_queue.append(node.left)
                next_queue.append(node.right)
                level_num.append(node.val)
        head, tail = 0, len(level_num) - 1
        while head < tail:
            if level_num[head] != level_num[tail]:
                return False
            head += 1
            tail -= 1
        queue = next_queue
    return True


def is_symmetric_tree_iterative2(root: TreeNode) -> bool:
    if root is None:
        return True
    stack = [root.left, root.right]
    while stack:
        p, q = stack.pop(), stack.pop()
        if p is None and q is None:
            continue
        if p is None or q is None or p.val != q.val:
            return False
        stack.append(p.left)
        stack.append(q.right)
        stack.append(p.right)
        stack.append(q.left)
    return True


def test_is_symmetric_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    assert is_symmetric_tree_recursive(root) is True
    assert is_symmetric_tree_iterative(root) is True
    assert is_symmetric_tree_iterative2(root) is True

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(3)
    assert is_symmetric_tree_recursive(root) is False
    assert is_symmetric_tree_iterative(root) is False
    assert is_symmetric_tree_iterative2(root) is False

    assert is_symmetric_tree_recursive(None) is True
    assert is_symmetric_tree_iterative(None) is True
    assert is_symmetric_tree_iterative2(None) is True


if __name__ == '__main__':
    test_is_symmetric_tree()
