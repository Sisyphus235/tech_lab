# -*- coding: utf8 -*-

"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false
Explanation: 14 is not ugly since it includes another prime factor 7.
Note:

1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−2^31,  2^31 − 1].
"""


def is_ugly(num: int) -> bool:
    if num <= 0:
        return False
    while num % 2 == 0:
        num //= 2
    while num % 3 == 0:
        num //= 3
    while num % 5 == 0:
        num //= 5
    return num == 1


def test_is_ugly():
    assert is_ugly(1) is True
    assert is_ugly(6) is True
    assert is_ugly(8) is True
    assert is_ugly(14) is False


if __name__ == '__main__':
    test_is_ugly()
