# -*- coding: utf8 -*-

"""
apply to large scale
best scenario: O(nlogn)
worst scenario: O(nlogn)
"""

import time
import random


def merge(array: list, left: int, mid: int, right: int):
    i, j = left, mid + 1
    tmp = []
    while i <= mid and j <= right:
        if array[i] <= array[j]:
            tmp.append(array[i])
            i += 1
        else:
            tmp.append(array[j])
            j += 1

    start = i if i <= mid else j
    end = mid if i <= mid else right
    tmp.extend(array[start: end + 1])
    array[left: right + 1] = tmp


def merge_sort_between(array: list, left: int, right: int):
    if left < right:
        mid = left + (right - left) // 2
        merge_sort_between(array, left, mid)
        merge_sort_between(array, mid + 1, right)
        merge(array, left, mid, right)


def merge_sort(array: list):
    merge_sort_between(array, 0, len(array) - 1)


def test_merge_sort():
    array = [random.randint(0, 100) for _ in range(100)]
    print(f'before: {array}')
    before = time.time()
    merge_sort(array)
    after = time.time()
    print(f'after: {array}')
    print(f'time cost: {after - before}')


if __name__ == '__main__':
    test_merge_sort()
