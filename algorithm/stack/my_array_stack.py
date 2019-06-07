# -*- coding: utf8 -*-

from typing import Optional


class ArrayStack:

    def __init__(self, size: int):
        self.size = size
        self._data = []

    def __repr__(self):
        return ' '.join(str(data) for data in self._data)

    @property
    def count(self):
        return len(self._data)

    def push(self, item: Optional) -> bool:
        if self.count == self.size:
            return False
        self._data.append(item)
        return True

    def pop(self) -> Optional:
        return self._data.pop()


def test_array_stack():
    array_stack = ArrayStack(3)
    assert array_stack.push(1) is True
    assert array_stack.push(2) is True
    assert array_stack.push(3) is True
    assert array_stack.push(4) is False
    assert array_stack.pop() == 3
    print(array_stack)


if __name__ == '__main__':
    test_array_stack()
