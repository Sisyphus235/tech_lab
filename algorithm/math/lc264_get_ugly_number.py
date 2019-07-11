# -*- coding: utf8 -*-

"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:

1 is typically treated as an ugly number.
n does not exceed 1690.

把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。例如 6、8 都是丑数，但 14 不是，因为它包含因子 7。
习惯上我们把 1 当做是第一个丑数。求按从小到大的顺序的第 N 个丑数。

剑指 offer 49
"""


def get_ugly_number(n: int) -> int:
    """
    维护一个丑数列表，寻找列表中的丑数乘以2，3，5后第一个大于当前丑数的值，三者中最小的是下一个丑数
    :param n:
    :return:
    """
    if n < 7:
        return n
    ugly_list = [i for i in range(7)]
    cur = 6
    while cur < n:
        mul2, mul3, mul5 = 0, 0, 0
        flag2, flag3, flag5 = True, True, True
        for i in range(cur - 1, 0, -1):
            if flag2 and ugly_list[i] * 2 <= ugly_list[cur]:
                mul2 = ugly_list[i + 1] * 2
                flag2 = False
            if flag3 and ugly_list[i] * 3 <= ugly_list[cur]:
                mul3 = ugly_list[i + 1] * 3
                flag3 = False
            if flag5 and ugly_list[i] * 5 <= ugly_list[cur]:
                mul5 = ugly_list[i + 1] * 5
                flag5 = False
            if not flag2 and not flag3 and not flag5:
                break
        ugly_list.append(min(mul2, mul3, mul5))
        cur += 1
    return ugly_list[-1]


def get_ugly_number2(n: int) -> int:
    ugly = [1]
    i2, i3, i5 = 0, 0, 0
    while n > 1:
        u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
        umin = min(u2, u3, u5)
        if umin == u2:
            i2 += 1
        if umin == u3:
            i3 += 1
        if umin == u5:
            i5 += 1
        ugly.append(umin)
        n -= 1
    return ugly[-1]


def test_get_ugly_number():
    assert get_ugly_number(1) == 1
    assert get_ugly_number2(1) == 1
    assert get_ugly_number(2) == 2
    assert get_ugly_number2(2) == 2
    assert get_ugly_number(3) == 3
    assert get_ugly_number2(3) == 3
    assert get_ugly_number(4) == 4
    assert get_ugly_number2(4) == 4
    assert get_ugly_number(5) == 5
    assert get_ugly_number2(5) == 5
    assert get_ugly_number(6) == 6
    assert get_ugly_number2(6) == 6
    assert get_ugly_number(7) == 8
    assert get_ugly_number2(7) == 8
    assert get_ugly_number(8) == 9
    assert get_ugly_number2(8) == 9
    assert get_ugly_number(9) == 10
    assert get_ugly_number2(9) == 10
    assert get_ugly_number(10) == 12
    assert get_ugly_number2(10) == 12
    assert get_ugly_number(507) == 1000000
    assert get_ugly_number2(507) == 1000000
    assert get_ugly_number(1297) == 301989888
    assert get_ugly_number2(1297) == 301989888


if __name__ == '__main__':
    test_get_ugly_number()
