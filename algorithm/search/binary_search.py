# -*- coding: utf8 -*-

import random
from algorithm.sort.shell_sort import shell_sort


def binary_search_between(array: list, low: int, high: int, value: int) -> int:
    if low > high:
        return -1
    # mid = low + (high - low) // 2
    mid = low + int((high - low) >> 1)
    if array[mid] == value:
        return mid
    elif array[mid] < value:
        return binary_search_between(array, mid + 1, high, value)
    else:
        return binary_search_between(array, low, mid - 1, value)


def binary_search_recursion(array: list, value: int) -> int:
    return binary_search_between(array, 0, len(array) - 1, value)


def binary_search_iteration(array: list, value: int) -> int:
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = low + int((high - low) >> 1)
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def test_binary_search():
    array = [random.randint(0, 100) for _ in range(100)]
    shell_sort(array)

    print(f'to search: {array}')
    assert binary_search_recursion(array, -2) == -1
    assert binary_search_recursion(array, 102) == -1
    index = binary_search_recursion(array, 66)
    print(f'index of 66 in recursion: {index}')

    assert binary_search_iteration(array, -2) == -1
    assert binary_search_iteration(array, 102) == -1
    index = binary_search_iteration(array, 66)
    print(f'index of 66 in iteration: {index}')


if __name__ == '__main__':
    test_binary_search()
