# -*- coding: utf8 -*-

"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor,
and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
"""

from typing import List


def min_cost_climbing_stairs(cost: List[int]) -> int:
    """
    状态方程：dp_array[n] = min((dp_array[n-1] + cost[n-1]), (dp[array[n-2], cost[n-2]))
    :param cost:
    :return:
    """
    length = len(cost)
    dp_array = [0] * (length + 1)
    dp_array[0], dp_array[1] = 0, 0
    for i in range(2, length + 1):
        dp_array[i] = min(dp_array[i - 1] + cost[i - 1], dp_array[i - 2] + cost[i - 2])
    return dp_array[-1]


def min_cost_climbing_stairs_2(cost: List[int]) -> int:
    """
    状态方程：dp_array[n] = cost[n] + min(dp_array[n-1], dp_array[n-2])
    :param cost:
    :return:
    """
    length = len(cost)
    dp_array = [0] * length
    dp_array[0], dp_array[1] = cost[0], cost[1]
    for i in range(2, length):
        dp_array[i] = cost[i] + min(dp_array[i - 1], dp_array[i - 2])
    return min(dp_array[-1], dp_array[-2])


def min_cost_climbing_stairs_space(cost: List[int]) -> int:
    """
    空间优化，存储前两个台阶的花销，空间复杂度 O(1)
    :param cost:
    :return:
    """
    length = len(cost)
    pre, cur = cost[0], cost[1]
    i = 2
    while i < length:
        pre, cur = cur, cost[i] + min(pre, cur)
        i += 1
    return min(pre, cur)


def test_min_cost_climbing_stairs():
    cost = [10, 15, 20]
    assert min_cost_climbing_stairs(cost) == 15
    assert min_cost_climbing_stairs_2(cost) == 15
    assert min_cost_climbing_stairs_space(cost) == 15

    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    assert min_cost_climbing_stairs(cost) == 6
    assert min_cost_climbing_stairs_2(cost) == 6
    assert min_cost_climbing_stairs_space(cost) == 6

    assert min_cost_climbing_stairs([0, 0, 1, 1]) == 1
    assert min_cost_climbing_stairs_2([0, 0, 1, 1]) == 1
    assert min_cost_climbing_stairs_space([0, 0, 1, 1]) == 1


if __name__ == '__main__':
    test_min_cost_climbing_stairs()
