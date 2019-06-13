# -*- coding: utf8 -*-

"""
full queue condition: tail == capacity
empty queue condition: head == tail
"""

from typing import Optional


class ArrayQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._data = [None] * capacity
        self.head = 0
        self.tail = 0

    def __repr__(self):
        return ' '.join(str(data) for data in self._data[self.head: self.tail])

    @property
    def count(self) -> int:
        return self.tail - self.head

    def clear(self):
        self._data = [None] * self.capacity
        self.head = self.tail = 0

    def enqueue(self, item: Optional) -> bool:
        if self.tail == self.capacity:
            if self.head == 0:
                return False
            for i in range(self.tail - self.head):
                self._data[i] = self._data[self.head + i]
            self.tail -= self.head
            self.head = 0
        self._data[self.tail] = item
        self.tail += 1
        return True

    def dequeue(self) -> Optional:
        if self.head == self.tail:
            return None
        ret = self._data[self.head]
        self.head += 1
        return ret


def test_array_queue():
    array_queue = ArrayQueue(3)
    assert array_queue.enqueue(1) is True
    assert array_queue.enqueue(2) is True
    assert array_queue.enqueue(3) is True
    assert array_queue.enqueue(4) is False
    assert array_queue.dequeue() == 1
    assert array_queue.count == 2
    print(array_queue)
    assert array_queue.enqueue(4) is True
    print(array_queue)
    array_queue.clear()
    assert array_queue.count == 0


if __name__ == '__main__':
    test_array_queue()
