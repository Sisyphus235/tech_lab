# -*- coding: utf8 -*-

"""
树的镜像，输入一个树的根，获得这棵树的镜像树
例如：
   2
 /  \
3   4
输出
   2
 /  \
4   3

剑指 offer 27
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_mirror_tree(root: TreeNode):
    if root is None:
        return
    swap_sub(root)
    get_mirror_tree(root.left)
    get_mirror_tree(root.right)


def swap_sub(root: TreeNode):
    tmp = root.left
    root.left = root.right
    root.right = tmp


def test_get_mirror_tree():
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(4)
    get_mirror_tree(root)
    assert root.left.val == 4
    assert root.right.val == 3

    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(4)
    root.right.left = TreeNode(5)
    get_mirror_tree(root)
    assert root.left.val == 4
    assert root.right.val == 3
    assert root.left.right.val == 5


if __name__ == '__main__':
    test_get_mirror_tree()
