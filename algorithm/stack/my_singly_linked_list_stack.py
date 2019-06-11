# -*- coding: utf8 -*-

from typing import Optional

from algorithm.linked_list.my_singly_linked_list import SinglyNode


class LinkedListStack:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self._top = None

    def __repr__(self):
        nodes = []
        while self._top:
            nodes.append(self._top.value)
            self._top = self._top.next
        return '->'.join(str(data) for data in nodes)

    @property
    def is_empty(self):
        return self._top is None

    def clear(self):
        self._top = None
        self.count = 0

    def push(self, item: Optional[int]) -> bool:
        if self.count == self.capacity:
            return False
        if self.is_empty:
            self._top = SinglyNode(item)
            self.count += 1
            return True
        new_node = SinglyNode(item)
        new_node.next = self._top
        self._top = new_node
        self.count += 1
        return True

    def pop(self) -> Optional[int]:
        if self.is_empty:
            return None
        rsp = self._top
        self._top = rsp.next
        self.count -= 1
        return rsp.value


def test_linked_list_stack():
    linked_list_stack = LinkedListStack(3)
    assert linked_list_stack.push(1) is True
    assert linked_list_stack.push(2) is True
    assert linked_list_stack.push(3) is True
    assert linked_list_stack.push(4) is False
    assert linked_list_stack.pop() == 3
    assert linked_list_stack.count == 2
    print(linked_list_stack)
    linked_list_stack.clear()
    assert linked_list_stack.count == 0


if __name__ == '__main__':
    test_linked_list_stack()
