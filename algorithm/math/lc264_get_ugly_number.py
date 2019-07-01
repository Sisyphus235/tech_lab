# -*- coding: utf8 -*-

"""
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

        ugly_list.append(min(mul2, mul3, mul5))
        cur += 1
    return ugly_list[-1]


def test_get_ugly_number():
    print(get_ugly_number(1))
    print(get_ugly_number(2))
    print(get_ugly_number(3))
    print(get_ugly_number(4))
    print(get_ugly_number(5))
    print(get_ugly_number(6))
    print(get_ugly_number(7))
    print(get_ugly_number(8))
    print(get_ugly_number(9))
    print(get_ugly_number(10))


if __name__ == '__main__':
    test_get_ugly_number()
