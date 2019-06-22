# -*- coding: utf8 -*-

"""
apply to special cases
best scenario: O(n)
worst scenario: O(n)
"""

import random
import time

from typing import List


def bucket_sort(array: List[int]):
    minimum, maximum = min(array), max(array)
    buckets = [0] * (maximum - minimum + 1)
    for i in range(len(array)):
        buckets[array[i] - minimum] += 1

    tmp = []
    for i in range(len(buckets)):
        if buckets[i] != 0:
            tmp += [i + minimum] * buckets[i]

    array[:] = tmp


def test_bucket_sort():
    array = [random.randint(0, 10) for _ in range(100)]
    length = len(array)

    print(f'before: {array}')
    before = time.time()
    bucket_sort(array)
    after = time.time()
    assert len(array) == length
    print(f'after: {array}')
    print(f'time cost: {after - before}')


if __name__ == '__main__':
    test_bucket_sort()
