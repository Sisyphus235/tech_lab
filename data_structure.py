# -*- coding: utf8 -*-


class Stack:
    def __init__(self, stack):
        """
        栈，初始化栈空间
        :param stack:
        """
        self.stack = stack if stack else []

    def is_empty(self):
        """
        判断栈是否空
        :return:
        """
        return False if self.stack else True

    def query(self):
        """
        查询栈
        :return:
        """
        return self.stack

    def push(self, element):
        """
        入栈
        :param element:
        :return:
        """
        self.stack.append(element)

    def pop(self):
        """
        出栈
        :return:
        """
        return self.stack.pop() if self.stack else None

    def peek(self):
        """
        查看栈顶元素
        :return:
        """
        return self.stack[-1] if self.stack else None


class LinkedListNode:
    def __init__(self, val=None):
        """
        节点，初始化节点值，节点next为None
        :param val:
        """
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def init_list(self, array):
        """
        根据传入列表初始化链表
        :param array:
        :return:
        """
        if not array:
            return
        self.head = LinkedListNode(array.pop(0))
        cur = self.head
        if array:
            for e in array:
                new = LinkedListNode(e)
                cur.next = new
                cur = cur.next

    def is_empty(self):
        return self.head is None

    def peek_first(self):
        if not self.head:
            return None
        return self.head.val

    def print_list(self, sep=', '):
        """
        以sep为分隔显示整个链表
        :param sep:
        :return:
        """
        if not self.head:
            print('')
            return
        cur = self.head
        values = []
        while cur:
            values.append(str(cur.val))
            cur = cur.next
        print(sep.join(values))

    def add_first(self, val):
        """
        在链表初始未知加入节点
        :param val:
        :return:
        """
        if not self.head:
            self.head = LinkedListNode(val)
            return
        new = LinkedListNode(val)
        new.next = self.head
        self.head = new

    def add_last(self, val):
        """
        在链表结尾位置加入节点
        :param val:
        :return:
        """
        if not self.head:
            self.head = LinkedListNode(val)
            return
        if not self.head.next:
            self.head.next = LinkedListNode(val)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = LinkedListNode(val)

    def remove_first(self):
        """
        在链表开始位置删除节点
        :return:
        """
        if not self.head:
            return
        if not self.head.next:
            val = self.head.val
            self.head = None
            return val
        val = self.head.val
        self.head = self.head.next
        return val

    def remove_last(self):
        """
        在链表结尾位置删除节点
        :return:
        """
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        cur = self.head
        while cur.next.next:
            cur = cur.next
        val = cur.next.val
        cur.next = None
        return val


class BinaryTree:
    """
    二叉树
    """

    def __init__(self, root_obj=None):
        self.root = root_obj
        self.left = None
        self.right = None

    def __str__(self, level=0, flag='r'):
        ret = "\t"*level + flag + repr(self.root) + "\n"
        if self.left:
            ret += self.left.__str__(level+1, 'l')
        if self.right:
            ret += self.right.__str__(level+1, 'r')

        return ret

    def __repr__(self, level=0, flag='r'):
        ret = "\t" * level + flag + repr(self.root) + "\n"
        if self.left:
            ret += self.left.__repr__(level + 1, 'l')
        if self.right:
            ret += self.right.__repr__(level + 1, 'r')

        return ret

    def insert_left(self, new):
        if self.left is None:
            self.left = BinaryTree(new)
        else:
            new_left = BinaryTree(new)
            new_left.left = self.left
            self.left = new_left

    def insert_right(self, new):
        if self.right is None:
            self.right = BinaryTree(new)
        else:
            new_right = BinaryTree(new)
            new_right.right = self.right
            self.right = new_right

    def get_height(self):
        """
        计算树的高度
        :param node:
        :return:
        """
        if self.root is None:
            return 0
        elif self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return 1 + self.right.get_height()
        elif self.right is None:
            return 1 + self.left.get_height()
        else:
            left = self.left.get_height()
            right = self.right.get_height()
            return 1 + max(left, right)

    def is_balanced(self):
        """
        计算数是否平衡，平衡的定义是任何node的左右分支高度相差小于等于1
        :return:
        """
        if self.root is None:
            return True
        elif self.left is None and self.right is None:
            return True
        elif self.left is None:
            return self.right.get_height() <= 1
        elif self.right is None:
            return self.left.get_height() <= 1
        else:
            left_height = self.left.get_height()
            right_height = self.right.get_height()
            if abs(left_height - right_height) > 1:
                return False
            else:
                return self.left.is_balanced() and self.right.is_balanced()
