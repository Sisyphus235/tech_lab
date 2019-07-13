# -*- coding: utf8 -*-

"""
Given an array of positive integers.
All numbers occur even number of times except one number which occurs odd number of times.
Find the number in O(n) time & constant space.

Examples :

Input : arr = {1, 2, 3, 2, 3, 1, 3}
Output : 3

Input : arr = {5, 7, 2, 7, 5, 2, 5}
Output : 5
"""


def odd_times_n_space(array: list) -> int:
    """
    space complexity: O(n)
    :param array:
    :return:
    """
    hash_space = {}
    for e in array:
        if e in hash_space:
            del hash_space[e]
        else:
            hash_space[e] = e
    return list(hash_space.values())[0]


def odd_times_1_space(array: list) -> int:
    """
    space complexity: O(1)
    XOR method, comply with commutative property
    :return:
    """
    for i in range(len(array) - 1):
        array[i + 1] = array[i] ^ array[i + 1]
    return array[-1]


def test_odd_times():
    array = [1, 2, 3, 2, 3, 1, 3]
    assert odd_times_n_space(array) == 3
    assert odd_times_1_space(array) == 3

    array = [5, 7, 2, 7, 5, 2, 5]
    assert odd_times_n_space(array) == 5
    assert odd_times_1_space(array) == 5


if __name__ == '__main__':
    test_odd_times()
