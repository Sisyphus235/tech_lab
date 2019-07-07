# -*- coding: utf8 -*-

"""
输入一个链表头结点，从尾到头反过来打印出每个结点的值
"""

from algorithm.linked_list.my_singly_linked_list import SinglyNode
from algorithm.stack.my_array_stack import ArrayStack


def reverse_print_stack(head: SinglyNode):
    stack = ArrayStack(10)
    while head:
        stack.push(head.value)
        head = head.next
    while not stack.is_empty:
        print(stack.pop())


def reverse_print_recursion(head: SinglyNode):
    if head.next:
        reverse_print_recursion(head.next)
    print(head.value)


def test_reverse_print():
    head = SinglyNode(5)
    head.next = SinglyNode(4)
    head.next.next = SinglyNode(3)
    head.next.next.next = SinglyNode(2)
    head.next.next.next.next = SinglyNode(1)
    reverse_print_stack(head)
    print()
    reverse_print_recursion(head)
    print()


if __name__ == '__main__':
    test_reverse_print()
