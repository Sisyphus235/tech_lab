# -*- coding: utf8 -*-

"""
一次爬 2/3 阶，多少种不同方案上 n 阶？n 是非负整数
"""


def two_three_climb(n: int) -> int:
    """
    状态方程：dp_array[n] = dp_array[n-2] + dp_array[n-3]
    :param n:
    :return:
    """
    if n < 2:
        return 0
    if n < 4:
        return 1
    dp_array = [0] * (n + 1)
    dp_array[2], dp_array[3] = 1, 1
    for i in range(4, n + 1):
        dp_array[i] = dp_array[i - 2] + dp_array[i - 3]
    return dp_array[n]


def test_two_tree_climb():
    assert two_three_climb(0) == 0
    assert two_three_climb(1) == 0
    assert two_three_climb(2) == 1  # 2
    assert two_three_climb(3) == 1  # 3
    assert two_three_climb(4) == 1  # 2,2
    assert two_three_climb(5) == 2  # 2,3 + 3,2
    assert two_three_climb(6) == 2  # 2,2,2 + 3,3
    assert two_three_climb(7) == 3  # 2,2,3 + 2,3,2 + 3,2,2


if __name__ == '__main__':
    test_two_tree_climb()
