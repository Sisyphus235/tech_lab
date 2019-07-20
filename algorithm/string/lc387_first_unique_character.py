# -*- coding: utf8 -*-

"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

剑指 offer 50
"""


def first_unique_character(s: str) -> int:
    ascii_list = [0] * 256
    for c in s:
        ascii_list[ord(c)] += 1
    for i in range(len(s)):
        if ascii_list[ord(s[i])] == 1:
            return i
    return -1


def test_first_unique_character():
    s = 'leetcode'
    assert first_unique_character(s) == 0

    s = 'loveleetcode'
    assert first_unique_character(s) == 2

    s = 'abba'
    assert first_unique_character(s) == -1


if __name__ == '__main__':
    test_first_unique_character()
