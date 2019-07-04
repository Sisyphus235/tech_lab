# -*- coding: utf8 -*-

"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

from typing import List
from copy import deepcopy


def minimum_total_dp(triangle: List[List[int]]) -> int:
    """
    状态方程：triangle[i][j] = min(triangle[i-1][j-1], triangle[i-1][j])
    :param triangle:
    :return:
    """
    dp_triangle = deepcopy(triangle)
    for i in range(1, len(dp_triangle)):
        for j in range(len(dp_triangle[i])):
            if j == 0:
                dp_triangle[i][j] += dp_triangle[i - 1][j]
            elif j == len(triangle[i]) - 1:
                dp_triangle[i][j] += dp_triangle[i - 1][j - 1]
            else:
                dp_triangle[i][j] += min(dp_triangle[i - 1][j - 1], dp_triangle[i - 1][j])
    # print(triangle)
    # print(dp_triangle)
    return min(dp_triangle[-1])


def minimum_total_space(triangle: List[List[int]]) -> int:
    """
    节省空间，空间复杂度是 O(1)，需要三角形最后一行大小的空间
    https://www.cnblogs.com/grandyang/p/4286274.html
    :param triangle:
    :return:
    """
    dp_array = triangle[-1]
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            dp_array[j] = min(dp_array[j], dp_array[j + 1]) + triangle[i][j]
    print(dp_array)
    return dp_array[0]


def test_minimum_total():
    array = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    assert minimum_total_dp(array) == 11
    assert minimum_total_space(array) == 11

    array = [
        [-1],
        [2, 3],
        [1, -1, -3],
        [5, 3, -1, 2]
    ]
    assert minimum_total_dp(array) == -2
    assert minimum_total_space(array) == -2


if __name__ == '__main__':
    """
    逆序遍历 range(len(array) - 1, -1, -1)
    """
    test_minimum_total()
