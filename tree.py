# -*- coding: utf8 -*-


from data_structure import BinaryTree


def binary_tree_pre_order_recursion(node):
    """
    前序遍历递归，根左右
    :param node:
    :return:
    """
    if node:
        print(node.root)
        binary_tree_pre_order_recursion(node.left)
        binary_tree_pre_order_recursion(node.right)


def binary_tree_pre_order_nonrecursion(node):
    """
    前序遍历非递归，根左右
    :param node:
    :return:
    """
    if node is None:
        return
    stack = [node]
    while stack:
        cur = stack.pop()
        print(cur.root)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)


if __name__ == '__main__':
    node = BinaryTree(1)
    node.left = BinaryTree(2)
    node.left.left = BinaryTree(3)
    node.left.right = BinaryTree(4)
    node.right = BinaryTree(5)
    node.right.right = BinaryTree(6)
    print('前序遍历：')
    # print(binary_tree_pre_order_recursion(node))
    print(binary_tree_pre_order_nonrecursion(node))
