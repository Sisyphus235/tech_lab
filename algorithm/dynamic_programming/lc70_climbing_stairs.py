# -*- coding: utf8 -*-

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


def climb_stairs_dp(n: int) -> int:
    """
    状态方程：dp_array[n] = dp_array[n-1] + dp_array[n-2]
    :param n:
    :return:
    """
    if n < 2:
        return n
    if n == 2:
        return 2
    dp_array = [0] * (n + 1)
    dp_array[1], dp_array[2] = 1, 2
    for i in range(3, n + 1):
        dp_array[i] = dp_array[i - 1] + dp_array[i - 2]
    print(dp_array)
    return dp_array[n]


def test_climb_stairs():
    assert climb_stairs_dp(0) == 0
    assert climb_stairs_dp(1) == 1
    assert climb_stairs_dp(2) == 2
    assert climb_stairs_dp(3) == 3
    assert climb_stairs_dp(4) == 5
    assert climb_stairs_dp(5) == 8
    assert climb_stairs_dp(10) == 55


if __name__ == '__main__':
    test_climb_stairs()
