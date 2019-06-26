# -*- coding: utf8 -*-


class LinkedNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class LinkedTree:
    def __init__(self):
        self.root = None

    @property
    def is_empty(self):
        return self.root is None

    def _print(self, node):
        if node is not None:
            self._print(node.left)
            print(str(node.value), ' ')
            self._print(node.right)

    def print(self):
        if self.is_empty:
            return ""
        return self._print(self.root)

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
    tree = LinkedTree()
    for i in range(10):
        tree.add(i)
    tree.print()


if __name__ == '__main__':
    test_linked_tree()
