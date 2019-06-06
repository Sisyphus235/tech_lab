# -*- coding: utf8 -*-

from typing import Optional

from algorithm.linked_list.my_linked_list import SingleLinkedList, SingleNode


def reverse_single_linked_list(head: SingleNode) -> Optional:
    """
    单链表反转，Leetcode 206
    :param head:
    :return:
    """
    try:
        pre = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        return pre
    except RuntimeError:
        return None


def test_reverse_single_linked_list():
    single_linked_list = SingleLinkedList()
    print(f'empty: {single_linked_list.get_all_nodes}')
    assert reverse_single_linked_list(single_linked_list.head) is None

    single_linked_list = SingleLinkedList()
    single_linked_list.insert_head(1)
    print(f'insert 1: {single_linked_list.get_all_nodes}')
    reverse = reverse_single_linked_list(single_linked_list.head)
    assert reverse.value == 1
    assert reverse.next is None

    single_linked_list = SingleLinkedList()
    single_linked_list.insert_head(1)
    single_linked_list.insert_head(3)
    print(f'insert 3: {single_linked_list.get_all_nodes}')
    reverse = reverse_single_linked_list(single_linked_list.head)
    assert reverse.value == 1
    assert reverse.next.value == 3
    assert reverse.next.next is None

    single_linked_list = SingleLinkedList()
    single_linked_list.insert_head(1)
    single_linked_list.insert_head(3)
    single_linked_list.insert_head(5)
    print(f'insert 5: {single_linked_list.get_all_nodes}')
    reverse = reverse_single_linked_list(single_linked_list.head)
    assert reverse.value == 1
    assert reverse.next.value == 3
    assert reverse.next.next.value == 5
    assert reverse.next.next.next is None


if __name__ == '__main__':
    test_reverse_single_linked_list()
