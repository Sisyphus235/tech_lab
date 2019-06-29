# -*- coding: utf8 -*-

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    match = {}
    for i, e in enumerate(nums):
        if target - e in match:
            return [match[target - e], i]
        match[e] = i


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


if __name__ == '__main__':
    """
    哈希存储目标值提高算法效率
    """
    test_two_sum()
