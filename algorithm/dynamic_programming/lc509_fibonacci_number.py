# -*- coding: utf8 -*-


def fibonacci_number_dp(n: int) -> int:
    """
    状态方程：dp[n] = dp[n-1] + dp[n-2]
    自底向上 dp[0] = 1, dp[1] = 1
    :param n:
    :return:
    """
    if n < 2:
        return n
    dp_array = [0] * (n + 1)
    dp_array[0], dp_array[1] = 0, 1
    for i in range(2, n + 1):
        dp_array[i] = dp_array[i - 1] + dp_array[i - 2]

    return dp_array[n]


def fibonacci_number_space(n: int) -> int:
    """
    节省空间，空间复杂度 O(1)
    :param n:
    :return:
    """
    if n < 2:
        return n
    pre, last = 0, 1
    cur = 1
    while cur < n:
        pre, last = last, pre + last
        cur += 1
    return last


def test_fibonacci_number():
    assert fibonacci_number_dp(0) == 0
    assert fibonacci_number_dp(1) == 1
    assert fibonacci_number_dp(2) == 1
    assert fibonacci_number_dp(3) == 2
    assert fibonacci_number_dp(4) == 3
    assert fibonacci_number_dp(5) == 5
    assert fibonacci_number_dp(10) == 55

    assert fibonacci_number_space(0) == 0
    assert fibonacci_number_space(1) == 1
    assert fibonacci_number_space(2) == 1
    assert fibonacci_number_space(3) == 2
    assert fibonacci_number_space(4) == 3
    assert fibonacci_number_space(5) == 5
    assert fibonacci_number_space(10) == 55


if __name__ == '__main__':
    """
    dp 先找到状态方程，返回值通常是 dp 容器的最后一两个
    """
    test_fibonacci_number()
