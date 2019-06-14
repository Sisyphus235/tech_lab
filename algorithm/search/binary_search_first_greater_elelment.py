# -*- coding: utf8 -*-

import random
from algorithm.sort.shell_sort import shell_sort


def binary_search_first_element(array: list, value: int) -> int:
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = low + int((high - low) >> 2)
        if array[mid] < value:
            low = mid + 1
        elif array[mid] > value:
            high = mid - 1
        else:
            if mid == 0 or array[mid - 1] != value:
                return mid
            else:
                high = mid - 1

    return -1


def test_binary_search_first_element():
    array = [random.randint(0, 10) for _ in range(20)]
    shell_sort(array)

    print(f'to search: {array}')
    assert binary_search_first_element(array, -2) == -1
    assert binary_search_first_element(array, 12) == -1
    index = binary_search_first_element(array, 2)
    print(f'index of first 2 is: {index}')


if __name__ == '__main__':
    test_binary_search_first_element()