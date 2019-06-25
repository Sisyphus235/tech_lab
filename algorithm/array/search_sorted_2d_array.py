# -*- coding: utf8 -*-

"""
一个包含整数的二维数组，左到右递增，上到下递增
判断一个整数是否在二维数组中
"""


def search_sorted_2d_array(array, n):
    row_len = len(array)
    col_len = len(array[0])
    row = 0
    col = col_len - 1

    while row < row_len and col >= 0:
        if array[row][col] == n:
            return True
        elif array[row][col] < n:
            row += 1
        else:
            col -= 1
    return False


def test_search_sorted_2d_array():
    array = [[1, 8, 9],
             [2, 10, 21],
             [5, 13, 35]]
    assert search_sorted_2d_array(array, 1) is True
    assert search_sorted_2d_array(array, 2) is True
    assert search_sorted_2d_array(array, 3) is False
    assert search_sorted_2d_array(array, 5) is True
    assert search_sorted_2d_array(array, 11) is False
    assert search_sorted_2d_array(array, 21) is True
    assert search_sorted_2d_array(array, 31) is False


if __name__ == '__main__':
    test_search_sorted_2d_array()
