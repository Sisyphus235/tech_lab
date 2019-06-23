# -*- coding: utf8 -*-

"""
apply to special cases
best scenario: O(n)
worst scenario: O(n)
"""

import random
import time

from typing import List


def counting_sort(array: List[int]):
    minimum = min(array)
    maximum = max(array)

    # generate count array
    count_array = [0] * (maximum - minimum + 1)
    for num in array:
        count_array[num] += 1
    # accumulate count array values
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]

    # sort array
    tmp = [0] * len(array)
    for num in reversed(array):
        idx = count_array[num] - 1
        tmp[idx] = num
        count_array[num] -= 1

    array[:] = tmp


def test_counting_sort():
    array = [random.randint(0, 10) for _ in range(100)]
    length = len(array)

    print(f'before: {array}')
    before = time.time()
    counting_sort(array)
    after = time.time()
    assert len(array) == length
    print(f'after: {array}')
    print(f'time cost: {after - before}')


if __name__ == '__main__':
    test_counting_sort()
