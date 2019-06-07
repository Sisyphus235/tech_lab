# -*- coding: utf8 -*-

from algorithm.linked_list.my_singly_linked_list import SinglyNode


def is_palindrome(head: SinglyNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    if fast:
        # odd number
        slow
    else:
        # even number
        pass
