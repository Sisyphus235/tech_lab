# -*- coding: utf8 -*-

"""
0，1，...，n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。
例如：
0-4 一个圈，每次删除第 3 个数字
0, 1, 2, 3, 4
第一次删除 2
3, 4, 0, 1
第二次删除 0
1, 3, 4
第三次删除 4
1, 3
第四次删除 1
3
最后返回 3

剑指 offer 62
"""

from algorithm.linked_list.my_singly_linked_list import SinglyNode


def last_num_in_circle_recursive(n: int, m: int) -> int:
    if n < 1 or m < 1:
        return -1
    if n == 1:
        return n
    return (last_num_in_circle_recursive(n - 1, m) + m) % n


def last_num_in_circle_iterative(n: int, m: int) -> int:
    if n < 1 or m < 1:
        return -1

    head = SinglyNode(0)
    cur = head
    for i in range(1, n + 1):
        cur.next = SinglyNode(i)
        cur = cur.next
    cur.next = head
    cur = head

    while True:
        if cur.next == cur:
            return cur.value
        for _ in range(m - 2):  # get the prev node of the one to be deleted
            cur = cur.next
        cur.next = cur.next.next


def test_last_num_in_circle():
    assert last_num_in_circle_recursive(4, 3) == 3
    assert last_num_in_circle_iterative(4, 3) == 3


if __name__ == '__main__':
    test_last_num_in_circle()
