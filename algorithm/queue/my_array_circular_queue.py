# -*- coding: utf8 -*-

"""
full queue condition: (tail + 1) % capacity == head
empty queue condition: tail == head
"""

from typing import Optional


class ArrayCircularQueue:
    def __init__(self, capacity: int):
        # sacrifice one position to avoid moving elements
        self.capacity = capacity + 1
        self._data = [None] * self.capacity
        self.head = 0
        self.tail = 0

    def __repr__(self):
        if self.head <= self.tail:
            return ' '.join(str(data) for data in self._data[self.head:self.tail])
        else:
            return ' '.join(str(data) for data in self._data[self.head:]) + ' ' + \
                   ' '.join(str(data) for data in self._data[:self.tail])

    @property
    def is_full(self) -> bool:
        return (self.tail + 1) % self.capacity == self.head

    @property
    def is_empty(self) -> bool:
        return self.head == self.tail

    @property
    def count(self):
        if self.head <= self.tail:
            return self.tail - self.head
        else:
            return self.capacity - (self.head - self.tail)

    def clear(self):
        self._data = [None] * self.capacity
        self.head = self.tail = 0

    def enqueue(self, item: Optional) -> bool:
        if self.is_full:
            return False
        self._data[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        return True

    def dequeue(self) -> Optional:
        if self.is_empty:
            return False
        ret = self._data[self.head]
        self.head = (self.head + 1) % self.capacity
        return ret


def test_array_circular_queue():
    array_circular_queue = ArrayCircularQueue(3)
    print(array_circular_queue)

    assert array_circular_queue.enqueue(0) is True
    assert array_circular_queue.enqueue(1) is True
    assert array_circular_queue.enqueue(2) is True
    assert array_circular_queue.enqueue(3) is False
    assert array_circular_queue.count == 3
    print(array_circular_queue)

    assert array_circular_queue.dequeue() == 0
    assert array_circular_queue.enqueue(4) is True
    assert array_circular_queue.count == 3
    assert array_circular_queue.dequeue() == 1
    assert array_circular_queue.dequeue() == 2
    assert array_circular_queue.count == 1
    assert array_circular_queue.enqueue(5) is True
    assert array_circular_queue.enqueue(6) is True
    print(array_circular_queue)

    array_circular_queue.clear()

    assert array_circular_queue.enqueue(0) is True
    assert array_circular_queue.enqueue(1) is True
    assert array_circular_queue.enqueue(2) is True
    assert array_circular_queue.enqueue(3) is False
    assert array_circular_queue.count == 3
    print(array_circular_queue)

    assert array_circular_queue.dequeue() == 0
    assert array_circular_queue.enqueue(4) is True
    assert array_circular_queue.count == 3
    assert array_circular_queue.dequeue() == 1
    assert array_circular_queue.dequeue() == 2
    assert array_circular_queue.count == 1
    assert array_circular_queue.enqueue(5) is True
    assert array_circular_queue.enqueue(6) is True
    print(array_circular_queue)


if __name__ == '__main__':
    test_array_circular_queue()
