# -*- coding: utf8 -*-


class BinaryTree:
    """
    二叉树
    """

    def __init__(self, root_obj=None):
        self.root = root_obj
        self.left = None
        self.right = None

    def __str__(self, level=0, flag='r'):
        ret = "\t" * level + flag + repr(self.root) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, 'l')
        if self.right:
            ret += self.right.__str__(level + 1, 'r')

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
