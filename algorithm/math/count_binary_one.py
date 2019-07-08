# -*- coding: utf8 -*-

"""
输入一个整数，输出该数二进制表示中 1 的个数。
剑指 offer 15
"""


def count_binary_one(n: int) -> int:
    """
    利用二进制运算特性寻找最后一个 1
    n      : 111000
    n-1    : 110111
    n & n-1: 110000
    :param n:
    :return:
    """
    count = 0
    while n:
        count += 1
        n = n & (n - 1)
    return count


def test_count_binary_one():
    assert count_binary_one(2) == 1  # 10
    assert count_binary_one(3) == 2  # 11
    assert count_binary_one(8) == 1  # 1000


if __name__ == '__main__':
    test_count_binary_one()
