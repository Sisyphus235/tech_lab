# -*- coding: utf8 -*-


from data_structure import BinaryTree


def binary_tree_pre_order_recursion(node):
    """
    前序遍历递归，根左右
    :param node:
    :return:
    """
    if node:
        print(node.root, end=', ')
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
        print(cur.root, end=', ')
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)


def binary_tree_mid_order_recursion(node):
    """
    中序遍历递归，左根右
    :param node:
    :return:
    """
    if node:
        binary_tree_mid_order_recursion(node.left)
        print(node.root, end=', ')
        binary_tree_mid_order_recursion(node.right)


def binary_tree_mid_order_nonrecursion(node):
    """
    中序遍历迭代，左根右
    :param node:
    :return:
    """
    stack = []
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print(node.root, end=', ')
            node = node.right


if __name__ == '__main__':
    node = BinaryTree(1)
    node.left = BinaryTree(2)
    node.left.left = BinaryTree(3)
    node.left.right = BinaryTree(4)
    node.right = BinaryTree(5)
    node.right.right = BinaryTree(6)

    pre_node = node
    print('前序遍历：')
    binary_tree_pre_order_nonrecursion(pre_node)
    print('')
    binary_tree_pre_order_recursion(pre_node)

    mid_node = node
    print('\n中序遍历：')
    binary_tree_mid_order_recursion(mid_node)
    print('')
    binary_tree_mid_order_nonrecursion(mid_node)
