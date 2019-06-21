# -*- coding: utf8 -*-

"""
apply to large scale
best scenario: O(nlogn)
worst scenario: O(n^2)
"""

import time
import random


def partition(array: list, left: int, right: int) -> int:
    pivot_value, j = array[left], left

    for i in range(left + 1, right + 1):
        if array[i] <= pivot_value:
            j += 1
            array[j], array[i] = array[i], array[j]
    array[left], array[j] = array[j], array[left]

    return j


def quick_sort_between(array: list, left: int, right: int):
    if left < right:
        random_pos = random.randint(left, right)
        array[left], array[random_pos] = array[random_pos], array[left]

        pivot = partition(array, left, right)
        quick_sort_between(array, left, pivot - 1)
        quick_sort_between(array, pivot + 1, right)


def quick_sort(array: list):
    quick_sort_between(array, 0, len(array) - 1)


def test_quick_sort():
    array = [random.randint(0, 100) for _ in range(100)]
    print(f'before: {array}')
    before = time.time()
    quick_sort(array)
    after = time.time()
    print(f'after: {array}')
    print(f'time cost: {after - before}')


if __name__ == '__main__':
    test_quick_sort()
    """
    lc215 kth largest element
    """
