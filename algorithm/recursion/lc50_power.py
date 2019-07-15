# -*- coding: utf8 -*-

"""
Implement pow(x, n), which calculates x raised to the power n (x^n).

Example 1:
Input: 2.00000, 10
Output: 1024.00000

Example 2:
Input: 2.10000, 3
Output: 9.26100

Example 3:
Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Note:
-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]

剑指 offer 16
"""


def power_recursion(x: float, n: int) -> float:
    if n == 0:
        return 1.0
    if n < 0:
        n = -n
        x = 1.0 / x
    mid = n // 2
    res = power_recursion(x, mid)
    if n & 1 == 0:  # if the binary of n "&" 1 is 0, the binary of n must be 0, n is even
        return res * res
    return res * res * x


def power_iteration(x: float, n: int) -> float:
    if n < 0:
        n = -n
        x = 1.0 / x
    ret = 1
    cur = x  # the crux, controlling even and odd multiple rules
    while n > 0:
        if n & 1 == 1:
            ret *= cur
        cur *= cur
        n //= 2
    return ret


def test_power():
    print(power_recursion(2.0000, 10))
    print(power_recursion(2.1000, 3))
    print(power_recursion(2.00000, -2))
    print(power_recursion(34.00515, -3))

    print(power_iteration(2.0000, 10))
    print(power_iteration(2.1000, 3))
    print(power_iteration(2.00000, -2))
    print(power_iteration(34.00515, -3))


if __name__ == '__main__':
    """
    1.幂指数有正负的情况，如果为负责将底数取倒数，幂指数统一为正数处理
    2.整数 //2 可以用位操作 >> 1
    3.判断奇偶性，用位操作 n & 1 == 1 是奇数， n & 1 == 0 是偶数
    """
    test_power()
