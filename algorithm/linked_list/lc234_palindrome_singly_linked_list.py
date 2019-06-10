# -*- coding: utf8 -*-

from algorithm.linked_list.my_singly_linked_list import SinglyNode, SinglyLinkedList
from algorithm.linked_list.lc206_reverse_singly_linked_list import reverse_single_linked_list


def is_palindrome(head: SinglyNode) -> bool:
    # find middle node of singly linked list
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse latter section of singly linked list according to odd or even attribute
    if fast:
        # odd number
        slow.next = reverse_single_linked_list(slow.next)
        slow = slow.next
    else:
        # even number
        slow = reverse_single_linked_list(slow)

    # compare front and latter nodes one by one
    while slow:
        if head.value != slow.value:
            return False
        head = head.next
        slow = slow.next
    return True


def test_is_palindrome():
    test_str_list = ['ab', 'aa', 'aba', 'abba', 'abcba']
    test_result_list = [False, True, True, True, True]

    for idx, case in enumerate(test_str_list):
        single_linked_list = SinglyLinkedList()
        for i in case:
            single_linked_list.insert_tail(i)
        print(f'initial status: {single_linked_list}')
        assert is_palindrome(single_linked_list.head) is test_result_list[idx]


if __name__ == '__main__':
    test_is_palindrome()
