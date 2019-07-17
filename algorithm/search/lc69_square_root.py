# -*- coding: utf8 -*-

"""
get the square root of some number, with accuracy of 6 digits after point
"""


def bisearch_square_root(num: float, precision: int) -> float:
    if num <= 0:
        return 0
    low, high = 0, num

    while low <= high:
        mid = low + (high - low) / 2
        cur = abs(mid ** 2 - num)
        if cur <= (10 ** -precision):
            return round(mid, precision)
        elif mid ** 2 < num:
            low = mid
        else:
            high = mid

    return 0


def newton_square_root(num: float, precision: int) -> float:
    if num <= 0:
        return 0
    guess = num
    while abs(guess ** 2 - num) > 10 ** (-precision):
        guess = (guess + (num / guess)) / 2  # improve guess by using average
    return round(guess, precision)


def test_square_root():
    nums = [-1.0, 0.0, 1.0, 8.0, 123.0, 346578.0, 312324.4546]
    precision = 6
    for num in nums:
        root = bisearch_square_root(num, precision)
        print(f'square root of {num} in bisearch is {root}')
        root = newton_square_root(num, precision)
        print(f'square root of {num} in newton is {root}')


def lc_sqrt(x: int) -> int:
    low, high = 0, x
    while low + 1 < high:
        mid = low + (high - low) // 2
        if mid ** 2 <= x:
            low = mid
        else:
            high = mid
    if high ** 2 <= x:
        return high
    return low


def my_sqrt(x: int) -> int:
    if x < 2:
        return x
    low, high = 0, x >> 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if mid * mid <= x:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1


def test_lc_sqrt():
    assert lc_sqrt(0) == 0
    assert lc_sqrt(1) == 1
    assert lc_sqrt(2) == 1
    assert lc_sqrt(4) == 2
    assert lc_sqrt(8) == 2
    assert lc_sqrt(2147395600) == 46340

    assert my_sqrt(0) == 0
    assert my_sqrt(1) == 1
    assert my_sqrt(2) == 1
    assert my_sqrt(4) == 2
    assert my_sqrt(8) == 2
    assert my_sqrt(2147395600) == 46340


if __name__ == '__main__':
    """
    技巧：注意位运算的优先级：low + ((high - low) >> 1) 不同于 low + (high - low) >> 1
    """
    test_square_root()
    test_lc_sqrt()
