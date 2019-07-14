# -*- coding: utf8 -*-

"""
Sort a linked list using insertion sort.


A graphical example of insertion sort.
The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data,
finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4

Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""

from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def insertion_sort_list(head: ListNode) -> ListNode:
    sentinel = ListNode(0)
    while head:
        tmp = head.next
        cur = sentinel
        while cur.next and cur.next.val <= head.val:
            cur = cur.next
        head.next = cur.next
        cur.next = head
        head = tmp

    return sentinel.next


def test_insertion_sort_list():
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    ret = insertion_sort_list(head)
    assert ret.val == 1
    assert ret.next.val == 2
    assert ret.next.next.val == 3
    assert ret.next.next.next.val == 4


if __name__ == '__main__':
    test_insertion_sort_list()
