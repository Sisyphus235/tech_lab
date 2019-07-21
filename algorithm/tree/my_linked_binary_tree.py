# -*- coding: utf8 -*-


class LinkedNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class LinkedBinaryTree:
    def __init__(self):
        self.root = None

    @property
    def is_empty(self):
        return self.root is None

    def _level(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        if node.left is None:
            return 1 + self._level(node.right)
        if node.right is None:
            return 1 + self._level(node.left)
        left_height = self._level(node.left)
        right_height = self._level(node.right)
        return 1 + max(left_height, right_height)

    @property
    def level(self):
        if self.is_empty:
            return 0
        return self._level(self.root)

    def _print(self, node, level, sign, ret):
        if node is not None:
            ret += '\t' * level + sign + str(node.value) + '\n'
            if node.left:
                ret += self._print(node.left, level + 1, 'l', ret)
            if node.right:
                ret += self._print(node.right, level + 1, 'r', ret)
            return ret

    def print(self):
        if self.is_empty:
            return ""
        return self._print(self.root, level=0, sign='', ret='')

    def _add(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = LinkedNode(value)
            else:
                self._add(value, node.left)
        else:
            if node.right is None:
                node.right = LinkedNode(value)
            else:
                self._add(value, node.right)

    def add(self, value):
        if self.is_empty:
            self.root = LinkedNode(value)
        else:
            self._add(value, self.root)

    def _find(self, value, node):
        if node.value == value:
            return node
        elif node.value < value and node.right is not None:
            self._find(value, node.right)
        elif node.value > value and node.left is not None:
            self._find(value, node.left)
        else:
            return None

    def find(self, value):
        if self.is_empty:
            return None
        return self._find(value, self.root)


def test_linked_tree():
    tree = LinkedBinaryTree()
    for i in [3, 5, 2, 4, 1, 7, 6]:
        tree.add(i)
    print(tree.level)
    tree.print()


if __name__ == '__main__':
    test_linked_tree()
