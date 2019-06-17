# -*- coding: utf8 -*-

"""
apply to small scale
best scenario: O(n^2)
worst scenario: O(n^2)
"""

import time
import random


def selection_sort(array: list):
    """
    best scenario: O(n^2)
    worst scenario: O(n^2)
    :param array:
    :return:
    """
    length = len(array)
    for i in range(length - 1):
        smallest = i
        for j in range(i + 1, length):
            if array[j] < array[smallest]:
                smallest = j
        if smallest != i:
            array[i], array[smallest] = array[smallest], array[i]


def test_selection_sort():
    array = [random.randint(0, 100) for _ in range(100)]
    print(f'before: {array}')
    before = time.time()
    selection_sort(array)
    after = time.time()
    print(f'after: {array}')
    print(f'time cost: {after - before}')


if __name__ == '__main__':
    test_selection_sort()
