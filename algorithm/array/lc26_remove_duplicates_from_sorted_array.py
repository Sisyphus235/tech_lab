# -*- coding: utf8 -*-

"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once
and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place
with O(1) extra memory.

Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5,
with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.

Clarification:
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference,
which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""

from typing import List


def remove_duplicates(nums: List[int]) -> int:
    length = len(nums)
    if length < 2:
        return length
    pre, cur = 1, 1
    while cur < length:
        if nums[cur] != nums[pre - 1]:
            nums[pre] = nums[cur]
            pre += 1
        cur += 1
    nums[:] = nums[:pre]
    return pre


def test_remove_duplicates():
    nums = [1, 1, 2]
    assert remove_duplicates(nums) == 2
    assert nums == [1, 2]

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert remove_duplicates(nums) == 5
    assert nums == [0, 1, 2, 3, 4]

    nums = []
    assert remove_duplicates(nums) == 0
    assert nums == []

    nums = [3]
    assert remove_duplicates(nums) == 1
    assert nums == [3]


if __name__ == '__main__':
    """
    双指针，一个遍历，一个在新数组插入位置，数组原位重新赋值 array[:] = xx
    """
    test_remove_duplicates()
