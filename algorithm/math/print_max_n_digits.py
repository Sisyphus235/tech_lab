# -*- coding: utf8 -*-

"""
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数即 999。
剑指 offer 17
"""


def print_max_n_digits(n: int) -> list:
    to_print = [0] * n
    ret = []
    while True:
        val = add_one(to_print)
        if val is False:
            return ret
        ret.append(val)


def add_one(array: list):
    length = len(array)
    cur = length - 1
    while cur >= 0:
        if array[cur] != 9:
            array[cur] += 1
            return ''.join(str(i) for i in array).lstrip('0')
        array[cur] = 0
        cur -= 1
    return False


def test_print_max_n_digits():
    print(print_max_n_digits(1))
    print(print_max_n_digits(2))
    print(print_max_n_digits(3))


if __name__ == '__main__':
    test_print_max_n_digits()
