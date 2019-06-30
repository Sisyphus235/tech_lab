# -*- coding: utf8 -*-

"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


def three_sum(nums: list) -> list:
    ret = []
    length = len(nums)
    nums = sorted(nums)
    for i in range(length - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        low = i + 1
        high = length - 1
        while low < high:
            value = nums[i] + nums[low] + nums[high]
            if value == 0:
                ret.append([nums[i], nums[low], nums[high]])
                while low < high and nums[low] == nums[low + 1]:
                    low += 1
                while low < high and nums[high] == nums[high - 1]:
                    high -= 1
                low += 1
                high -= 1
            elif value < 0:
                low += 1
            else:
                high -= 1
    return ret


def test_three_sum():
    print(three_sum([-1, 0, 1, 2, -1, -4]))
    print(three_sum([1, 1, 1]))
    print(three_sum([-2, 0, 1, 1, 2]))


if __name__ == '__main__':
    """
    有序数组可以用头尾指针，相同节点判断可以剪枝提升算法效率
    """
    test_three_sum()
