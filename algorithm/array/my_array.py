# -*- coding: utf8 -*-

"""
Realize insertion, delete and random access of array, ignoring negative index
"""

from typing import Optional


class MyArray:
    def __init__(self, capacity: int):
        self._data = []
        self._capacity = capacity

    def __getitem__(self, position: int) -> Optional[int]:
        return self._data[position]

    def __setitem__(self, index: int, value: Optional[int]):
        self._data[index] = value

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            yield item

    def __repr__(self):
        return ' '.join(str(data) for data in self._data)

    def find(self, index: int) -> Optional[int]:
        try:
            return self._data[index]
        except IndexError:
            return None

    def delete(self, index: int) -> bool:
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False

    def insert(self, index: int, value: Optional[int]) -> bool:
        if len(self) >= self._capacity:
            return False

        self._data.insert(index, value)
        return True

    def print_all(self):
        for item in self._data:
            print(item)


def test_myarray():
    array = MyArray(10)
    assert array.insert(0, 1) is True
    assert array.find(0) == 1
    assert array.delete(0) is True
    assert array.delete(0) is False
    array.insert(0, 1)
    array.insert(1, 3)
    array.insert(2, 5)
    array.print_all()
    print(array)


if __name__ == '__main__':
    test_myarray()
