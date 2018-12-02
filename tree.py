# -*- coding: utf8 -*-


from data_structure import BinaryTree


def binary_tree_pre_order_recursion(node, record=[]):
    """
    前序遍历递归，根左右
    """
    if node:
        print(node.root, end=', ')
        record.append(node.root)
        binary_tree_pre_order_recursion(node.left)
        binary_tree_pre_order_recursion(node.right)

    return record


def binary_tree_pre_order_nonrecursion(node):
    """
    前序遍历非递归，根左右
    1. 利用栈，对每一个结点，先输出结点内容；
    2. 若右子树不为空，右子树压栈；
    3. 若左子树不为空，左子树压栈。
    """
    if node is None:
        return
    stack = [node]
    record = []
    while stack:
        cur = stack.pop()
        print(cur.root, end=', ')
        record.append(cur.root)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)

    return record


def binary_tree_mid_order_recursion(node, record=[]):
    """
    中序遍历递归，左根右
    :param node:
    :return:
    """
    if node:
        binary_tree_mid_order_recursion(node.left)
        print(node.root, end=', ')
        record.append(node.root)
        binary_tree_mid_order_recursion(node.right)

    return record


def binary_tree_mid_order_nonrecursion(node):
    """
    中序遍历迭代，左根右
    左子树不断入栈直到没有左子树，输出当前结点内容并指向右子树
    :param node:
    :return:
    """
    stack = []
    record = []
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print(node.root, end=', ')
            record.append(node.root)
            node = node.right

    return record


def binary_tree_post_order_recursion(node, record=[]):
    """
    后序遍历递归，左右根
    :param node:
    :return:
    """
    if node:
        binary_tree_post_order_recursion(node.left)
        binary_tree_post_order_recursion(node.right)
        print(node.root, end=', ')
        record.append(node.root)

    return record


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
    record = []
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
            record.append(flag.root)

    return record


if __name__ == '__main__':
    node = BinaryTree(1)
    node.insert_left(2)
    node.insert_right(6)
    node.insert_right(5)
    left = node.left
    left.insert_left(3)
    left.insert_right(4)

    pre_node = node
    print('前序遍历：')  # 根 -> 左 -> 右，根在最前面
    record = binary_tree_pre_order_recursion(pre_node)
    print(f'\nrecord: {record}')
    record = binary_tree_pre_order_nonrecursion(pre_node)
    print(f'\nrecord: {record}')

    mid_node = node
    print('\n中序遍历：')  # 左 -> 根 -> 右，根在中间
    record = binary_tree_mid_order_recursion(mid_node)
    print(f'\nrecord: {record}')
    record = binary_tree_mid_order_nonrecursion(mid_node)
    print(f'\nrecord: {record}')

    post_node = node
    print('\n后序遍历：')  # 左 -> 右 -> 根，根在后面
    record = binary_tree_post_order_recursion(post_node)
    print(f'\nrecord: {record}')
    record = binary_tree_post_order_nonrecursion(post_node)
    print(f'\nrecord: {record}')
