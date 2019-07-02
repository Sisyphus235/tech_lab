# -*- coding: utf8 -*-

"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    history = set()
    for e in nums:
        if e not in history:
            history.add(e)
        else:
            return True
    return False


def test_contains_duplicate():
    nums = [1, 2, 3, 1]
    assert contains_duplicate(nums) is True

    nums = [1, 2, 3, 4]
    assert contains_duplicate(nums) is False

    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    assert contains_duplicate(nums) is True


if __name__ == '__main__':
    test_contains_duplicate()
