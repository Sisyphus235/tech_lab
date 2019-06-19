# -*- coding: utf8 -*-

"""
advanced insertion sort
apply to small scale
best scenario: O(n)
worst scenario: < O(n^2), approach to O(nlogn)
"""

import time
import random


def shell_sort(array: list):
    # group gap
    gap = len(array) // 2
    # loop until gap equals to 1, all array will be sorted
    while gap > 0:
        # sort all groups in one loop, increase 1 each time, perhaps operating insertion sort to different groups
        for i in range(gap, len(array)):
            j = i
            # operating insertion sort based on groups
            while j > 0 and array[j] < array[j - gap]:
                array[j], array[j - gap] = array[j - gap], array[j]
                j -= gap
        gap //= 2


def test_shell_sort():
    array = [random.randint(0, 100) for _ in range(100)]
    print(f'before: {array}')
    before = time.time()
    shell_sort(array)
    after = time.time()
    print(f'after: {array}')
    print(f'time cost: {after - before}')


if __name__ == '__main__':
    test_shell_sort()
