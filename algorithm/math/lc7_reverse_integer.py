# -*- coding: utf8 -*-


"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


def reverse_integer(x: int) -> int:
    max_int = 2 ** 31 - 1
    min_int = - 2 ** 31
    ret = 0
    sign = 1
    if x < 0:
        sign = -1
        x = -x
    while x:
        val = x % 10
        ret = ret * 10 + val
        if sign * ret >= max_int or sign * ret <= min_int:
            return 0
        x //= 10

    return ret * sign


def test_reverse_integer():
    assert reverse_integer(123) == 321
    assert reverse_integer(-123) == -321
    assert reverse_integer(120) == 21
    assert reverse_integer(1534236469) == 0


if __name__ == '__main__':
    """
    数字有正负区分的时候，用 sign = +/-1 来记录，把负数变成正数统一处理
    while 循环，永远先记得先写修改循环判断条件的表达式
    """
    test_reverse_integer()
