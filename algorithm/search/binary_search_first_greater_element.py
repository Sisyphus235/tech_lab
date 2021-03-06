# -*- coding: utf8 -*-

import random
from algorithm.sort.shell_sort import shell_sort


def binary_search_first_greater_element(array: list, value: int) -> int:
    """
    search the first element whose value is greater than input value
    :param array:
    :param value:
    :return:
    """
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = low + int((high - low) >> 1)
        if array[mid] > value:
            if mid == 0 or array[mid - 1] <= value:
                return mid
            high = mid - 1
        else:
            low = mid + 1
    return -1


def test_binary_search_first_greater_element():
    array = [random.randint(0, 10) for _ in range(20)]
    shell_sort(array)

    print(f'to search: {array}')
    index = binary_search_first_greater_element(array, 2)
    print(f'index of first element greater than 2 is: {index}')


if __name__ == '__main__':
    test_binary_search_first_greater_element()
