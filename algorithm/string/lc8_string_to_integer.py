# -*- coding: utf8 -*-

"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible,
and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number,
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number,
or if no such sequence exists because either str is empty or it contains only whitespace characters,
no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−231,  231 − 1].
If the numerical value is out of the range of representable values, INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.

Example 1:
Input: "42"
Output: 42

Example 2:
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.

Example 3:
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.

Example 5:
Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
"""


def atoi(str: str) -> int:
    def value_check(str: str, start: int, end: int) -> int:
        if start == -1:
            return 0
        str_value = str[start: end]
        if str_value == '+' or str_value == '-':
            return 0
        return int(str_value)

    min_int = - 2 ** 31
    max_int = 2 ** 31 - 1
    numbers = '0123456789'
    sign = ['+', '-']

    point, start = 0, -1
    while point < len(str):
        if start == -1:
            if str[point] == ' ':
                point += 1
                continue
            elif str[point] in sign or str[point] in numbers:
                start = point
                point += 1
                continue
            else:
                return 0
        elif str[point] in numbers:
            value = int(str[start:point + 1])
            if value <= min_int:
                return min_int
            if value >= max_int:
                return max_int
            point += 1
        else:
            return value_check(str, start, point)
    return value_check(str, start, point)


def atoi2(str: str) -> int:
    min_int = - 2 ** 31
    max_int = 2 ** 31 - 1
    result = 0

    if not str:
        return result

    i = 0
    while i < len(str) and str[i] == ' ':
        i += 1

    if i >= len(str):
        return result

    sign = 1
    if str[i] == '+':
        i += 1
    elif str[i] == '-':
        i += 1
        sign = -1

    while i < len(str) and '0' <= str[i] <= '9':
        if result * 10 + int(str[i]) > max_int:
            return max_int if sign > 0 else min_int
        result = result * 10 + int(str[i])
        i += 1

    return sign * result


def test_atoi():
    assert atoi('42') == 42
    assert atoi("  -42") == -42
    assert atoi("4193 with words") == 4193
    assert atoi("words and 987") == 0
    assert atoi("-91283472332") == -2147483648
    assert atoi('') == 0
    assert atoi('+') == 0
    assert atoi('-') == 0
    assert atoi(' ') == 0

    assert atoi2('42') == 42
    assert atoi2("  -42") == -42
    assert atoi2("4193 with words") == 4193
    assert atoi2("words and 987") == 0
    assert atoi2("-91283472332") == -2147483648
    assert atoi2('') == 0
    assert atoi2('+') == 0
    assert atoi2('-') == 0
    assert atoi2(' ') == 0


if __name__ == '__main__':
    """
    复杂条件判断时，用 while 循环更容易区分不同条件，而不是用 for 循环加很多 if
    """
    test_atoi()
