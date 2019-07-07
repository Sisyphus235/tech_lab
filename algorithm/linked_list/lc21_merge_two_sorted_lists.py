# -*- coding: utf8 -*-

"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

from algorithm.linked_list.my_singly_linked_list import SinglyNode


def merge_two_lists(l1: SinglyNode, l2: SinglyNode) -> SinglyNode:
    sentinel = SinglyNode(0)
    cur = sentinel

    while l1 and l2:
        if l1.value <= l2.value:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next

    cur.next = l1 or l2
    return sentinel.next


def test_merge_two_lists():
    h1 = SinglyNode(1)
    h1.next = SinglyNode(2)
    h1.next.next = SinglyNode(4)

    h2 = SinglyNode(1)
    h2.next = SinglyNode(3)
    h2.next.next = SinglyNode(4)

    ret = merge_two_lists(h1, h2)
    assert ret.value == 1
    assert ret.next.value == 1
    assert ret.next.next.value == 2
    assert ret.next.next.next.value == 3
    assert ret.next.next.next.next.value == 4
    assert ret.next.next.next.next.next.value == 4


if __name__ == '__main__':
    """
    用 sentinel 标记返回结果的初始前一位，方便找到节点
    """
    test_merge_two_lists()
