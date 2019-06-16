# -*- coding: utf8 -*-

"""
apply to small scale
best scenario: O(n)
worst scenario: O(n^2)
"""

import time
import random


def bubble_sort(array: list):
    length = len(array)
    for i in range(length - 1):
        has_switch = False
        for j in range(length - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                has_switch = True
        # if no switch, no need to continue the algorithm
        if not has_switch:
            break


def test_bubble_sort():
    array = [random.randint(0, 100) for _ in range(100)]
    print(f'before: {array}')
    before = time.time()
    bubble_sort(array)
    after = time.time()
    print(f'after: {array}')
    print(f'time cost: {after - before}')


if __name__ == '__main__':
    test_bubble_sort()
