# -*- coding: utf8 -*-

from typing import Optional

from algorithm.linked_list.my_singly_linked_list import SinglyNode


class SinglyLinkedListQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None

    def __repr__(self):
        return '->'.join(str(data) for data in self._get_all_nodes())

    def _get_all_nodes(self) -> list:
        all_nodes = []
        cur = self.head
        while cur:
            all_nodes.append(cur.value)
            cur = cur.next
        return all_nodes

    @property
    def count(self) -> int:
        return len(self._get_all_nodes())

    @property
    def is_full(self) -> bool:
        return self.count == self.capacity

    @property
    def is_empty(self):
        return self.count == 0

    def clear(self):
        self.head = self.tail = None

    def enqueue(self, item: Optional) -> bool:
        if self.is_full:
            return False
        if self.is_empty:
            self.head = self.tail = SinglyNode(item)
        else:
            new_node = SinglyNode(item)
            self.tail.next = new_node
            self.tail = new_node
        return True

    def dequeue(self) -> Optional:
        if self.is_empty:
            return None
        ret = self.head.value
        if self.count == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        return ret


def test_singly_linked_list_queue():
    singly_linked_list_queue = SinglyLinkedListQueue(3)
    print(singly_linked_list_queue)

    assert singly_linked_list_queue.enqueue(0) is True
    assert singly_linked_list_queue.enqueue(1) is True
    assert singly_linked_list_queue.enqueue(2) is True
    assert singly_linked_list_queue.enqueue(3) is False
    print(singly_linked_list_queue)

    assert singly_linked_list_queue.dequeue() == 0
    assert singly_linked_list_queue.count == 2
    print(singly_linked_list_queue)

    assert singly_linked_list_queue.enqueue(3) is True
    print(singly_linked_list_queue)

    singly_linked_list_queue.clear()
    assert singly_linked_list_queue.count == 0


if __name__ == '__main__':
    test_singly_linked_list_queue()
