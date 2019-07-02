# -*- coding: utf8 -*-

"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

from typing import List


def majority_element(nums: List[int]) -> int:
    length = len(nums)
    bar = length // 2 + 1 if length & 1 else length // 2
    stat = {}
    for num in nums:
        stat.setdefault(num, 0)
        if stat[num] >= bar - 1:
            return num
        stat[num] += 1


def test_majority_element():
    nums = [3, 2, 3]
    assert majority_element(nums) == 3

    nums = [2, 2, 1, 1, 1, 2, 2]
    assert majority_element(nums) == 2


if __name__ == '__main__':
    test_majority_element()
