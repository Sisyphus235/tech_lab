# -*- coding: utf8 -*-

"""
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared
at most twice and return the new length.

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,1,2,2,3],
Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,0,1,1,1,1,2,3,3],
Your function should return length = 7,
with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.
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

MOST = 2


def remove_duplicates(nums: List[int]) -> int:
    length = len(nums)
    if length < 3:
        return length
    pre, cur = 2, 2
    while cur < length:
        if not (nums[cur] == nums[pre - 1] and nums[cur] == nums[pre - 2]):
            nums[pre] = nums[cur]
            pre += 1
        cur += 1
    nums[:] = nums[:pre]
    return pre


def remove_duplicates_count(nums: List[int]) -> int:
    length = len(nums)
    if length < 3:
        return length
    cur = 1
    count = 2 if nums[cur] == nums[cur - 1] else 1
    cur += 1
    pre = cur
    while cur < length:
        if nums[cur] == nums[pre - 1]:
            if count != MOST:
                count += 1
                nums[pre] = nums[cur]
                pre += 1
        else:
            count = 1
            nums[pre] = nums[cur]
            pre += 1
        cur += 1
    nums[:] = nums[:pre]
    return pre


def test_remove_duplicates():
    nums = [1, 1, 1, 2, 2, 3]
    assert remove_duplicates(nums) == 5
    assert nums == [1, 1, 2, 2, 3]

    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    assert remove_duplicates(nums) == 7
    assert nums == [0, 0, 1, 1, 2, 3, 3]

    nums = []
    assert remove_duplicates(nums) == 0
    assert nums == []

    nums = [6]
    assert remove_duplicates(nums) == 1
    assert nums == [6]

    nums = [6, 7]
    assert remove_duplicates(nums) == 2
    assert nums == [6, 7]

    nums = [6, 6]
    assert remove_duplicates(nums) == 2
    assert nums == [6, 6]

    nums = [1, 1, 1, 2, 2, 3]
    assert remove_duplicates_count(nums) == 5
    assert nums == [1, 1, 2, 2, 3]

    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    assert remove_duplicates_count(nums) == 7
    assert nums == [0, 0, 1, 1, 2, 3, 3]

    nums = []
    assert remove_duplicates_count(nums) == 0
    assert nums == []

    nums = [6]
    assert remove_duplicates_count(nums) == 1
    assert nums == [6]

    nums = [6, 7]
    assert remove_duplicates_count(nums) == 2
    assert nums == [6, 7]

    nums = [6, 6]
    assert remove_duplicates_count(nums) == 2
    assert nums == [6, 6]


if __name__ == '__main__':
    test_remove_duplicates()
