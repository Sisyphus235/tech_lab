# -*- coding: utf8 -*-

import random
from algorithm.sort.shell_sort import shell_sort


def binary_search_last_less_element(array: list, value: int) -> int:
    """
    search the last element whose value is less than input value
    :param array:
    :param value:
    :return:
    """
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = low + int((high - low) >> 1)
        if array[mid] < value:
            if mid == len(array) - 1 or array[mid + 1] >= value:
                return mid
            low = mid + 1
        else:
            high = mid - 1
    return -1


def test_binary_search_last_less_element():
    array = [random.randint(0, 10) for _ in range(20)]
    shell_sort(array)

    print(f'to search: {array}')
    index = binary_search_last_less_element(array, 2)
    print(f'index of last less than 2 is: {index}')


if __name__ == '__main__':
    test_binary_search_last_less_element()
