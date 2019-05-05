# -*- coding: utf8 -*-

"""
输入一个字符串，全部由 0 和 1 构成，寻找一个子字符，
使得这个子字符串中 0 和 1 的数量相等，
求子字符串最大长度。

Example
11010111110
最大长度为 4，可以是 1010 （第 2 到 第 5 位），
或者是 0101 （第 3 到 第 6 位）
"""


def longest_substring_equally_0_1(s: str):
    # record of difference of 1 and 0
    one_minus_zero = 0
    # record of the first position of the difference
    first_occurrence = {}
    # record of the maximum length of substring whose number of 1 equals to 0
    max_length = 0

    for i, num in enumerate(s):
        if num == "1":
            one_minus_zero += 1
        else:
            one_minus_zero -= 1

        current_difference = abs(one_minus_zero)
        if current_difference not in first_occurrence:
            first_occurrence[current_difference] = i
        else:
            current_length = i - first_occurrence[current_difference]
            max_length = max(max_length, current_length)

    return max_length


if __name__ == '__main__':
    print(longest_substring_equally_0_1("11010111110"))
    print(longest_substring_equally_0_1("110100111110"))
