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
    1. 利用栈，对每一个结点，先输出结点内容；
    2. 若右子树不为空，右子树压栈；
    3. 若左子树不为空，左子树压栈。
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
    左子树不断入栈直到没有左子树，输出当前结点内容并指向右子树
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


def binary_tree_post_order_recursion(node):
    """
    后序遍历递归，左右根
    :param node:
    :return:
    """
    if node:
        binary_tree_post_order_recursion(node.left)
        binary_tree_post_order_recursion(node.right)
        print(node.root, end=', ')


def binary_tree_post_order_nonrecursion(node):
    """
    后序遍历迭代，左右根
    1.利用栈和一个标记结点(初始化为None)
    2.对每一个结点，左子树不断入栈直到没有左子树
    3.此时如果栈顶节点右子树不等于标记结点，
    栈顶节点右子树入栈，标记节点置None
    4.否则(即没有右子树或者右子树等于标记节点),
    利用标记节点输出栈顶结点内容

    说明，标记节点的作用是为了标记已经输入的结点，防止死循环
    :param node:
    :return:
    """
    stack = []
    flag = None
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        elif stack[-1].right != flag:
            stack.append(stack[-1].right)
            flag = None
        else:
            flag = stack.pop()
            print(flag.root, end=', ')


if __name__ == '__main__':
    node = BinaryTree(1)
    node.left = BinaryTree(2)
    node.left.left = BinaryTree(3)
    node.left.right = BinaryTree(4)
    node.right = BinaryTree(5)
    node.right.right = BinaryTree(6)

    pre_node = node
    print('前序遍历：')  # 根 -> 左 -> 右，根在最前面
    binary_tree_pre_order_nonrecursion(pre_node)
    print('')
    binary_tree_pre_order_recursion(pre_node)

    mid_node = node
    print('\n中序遍历：')  # 左 -> 根 -> 右，根在中间
    binary_tree_mid_order_recursion(mid_node)
    print('')
    binary_tree_mid_order_nonrecursion(mid_node)

    post_node = node
    print('\n后序遍历：')  # 左 -> 右 -> 根，根在后面
    binary_tree_post_order_recursion(post_node)
    print('')
    binary_tree_post_order_nonrecursion(post_node)
