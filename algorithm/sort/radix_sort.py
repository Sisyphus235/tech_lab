# -*- coding: utf8 -*-

"""
n digits int sorting
best scenario: O(n)
worst scenario: O(n)
"""

import random
import time

from typing import List


def radix_sort(array: List[int], digits: int):
    for i in range(digits):
        # 0-9, total 10 digits mapping to 10 buckets
        buckets = [[] for _ in range(10)]
        for num in array:
            buckets[num // (10 ** i) % 10].append(num)
        array[:] = [num for bucket in buckets for num in bucket]


def test_radix_sort():
    array = [random.randint(100, 999) for _ in range(100)]
    length = len(array)

    print(f'before: {array}')
    before = time.time()
    radix_sort(array, 3)
    after = time.time()
    assert len(array) == length
    print(f'after: {array}')
    print(f'time cost: {after - before}')


if __name__ == '__main__':
    test_radix_sort()
