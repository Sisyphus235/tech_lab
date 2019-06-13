# -*- coding: utf8 -*-

"""
apply to large scale
best scenario: O(nlogn)
worst scenario: O(nlogn)
"""

import time
import random


def merge(left: list, right: list) -> list:
    after_merge = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            after_merge.append(left[l])
            l += 1
        else:
            after_merge.append(right[r])
            r += 1
    after_merge = after_merge + left[l:] + right[r:]
    return after_merge


def merge_sort(array: list) -> list:
    length = len(array)
    if length <= 1:
        return array
    mid = length // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)


def test_merge_sort():
    array = [random.randint(0, 100) for _ in range(100)]
    print(f'before: {array}')
    before = time.time()
    array = merge_sort(array)
    after = time.time()
    print(f'after: {array}')
    print(f'time cost: {after - before}')


if __name__ == '__main__':
    test_merge_sort()
