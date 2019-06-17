# -*- coding: utf8 -*-

"""
apply to small scale
best scenario: O(n)
worst scenario: O(n^2)
"""

import time
import random


def insertion_sort(array: list):
    length = len(array)
    for i in range(1, length):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1


def test_insertion_sort():
    array = [random.randint(0, 100) for _ in range(100)]
    print(f'before: {array}')
    before = time.time()
    insertion_sort(array)
    after = time.time()
    print(f'after: {array}')
    print(f'time cost: {after - before}')


if __name__ == '__main__':
    test_insertion_sort()
