# -*- coding: utf8 -*-


import time
from data_structure import LinkedList


def remove_dup(linkedlist):
    """
    不使用buffer删除链表中重复值，2.1
    :param linkedlist:
    :return:
    """
    if not linkedlist.head:
        return linkedlist
    cur = linkedlist.head
    while cur:
        check = cur
        while check.next:
            if check.next.val == cur.val:
                check.next = check.next.next
            else:
                check = check.next
        cur = cur.next
    return linkedlist


def k2last(linkedlist, k):
    """
    查找倒数第K个到最后一个节点的value array, 2.2
    :param linkedlist:
    :param k:
    :return:
    """
    rtn = []
    second = linkedlist.head
    while k > 0:
        if not second:
            return "not enough nodes"
        second = second.next
        k -= 1
    first = linkedlist.head
    while second:
        first = first.next
        second = second.next
    while first:
        rtn.append(first.val)
        first = first.next
    return rtn


def del_middle_node(linkedlistNode):
    """
    只有当前点的信息，在链表中删除这个节点，2.3
    :param linkedlistNode:
    :return:
    """
    cur, next = linkedlistNode, linkedlistNode.next
    if not next:
        return None
    while next:
        cur.val = next.val
        cur = next
        next = next.next


def partition_linked_list(linkedlist, val):
    """
    分割链表，小于val的放在前面，大于的放在后面，2.4
    :param linkedlist:
    :param val:
    :return:
    """
    small = LinkedList()
    small.init_list([-1])
    small_cur = small.head
    large = LinkedList()
    large.init_list([-1])
    large_cur = large.head

    cur = linkedlist.head
    if not cur:
        return None
    while cur:
        cur_val = cur.val
        if cur_val <= val:
            small_cur.next = cur
            small_cur = cur
            cur = cur.next
            small_cur.next = None
        else:
            large_cur.next = cur
            large_cur = cur
            cur = cur.next
            large_cur.next = None

    if small_cur != small.head:
        small.head = small.head.next
        if large_cur != large.head:
            small_cur.next = large.head.next
        return small
    else:
        large.head = large.head.next
        return large


class AnimalShelter:
    """
    3.7, 用链表模仿宠物收容所
    """

    def __init__(self):
        self.dogs = LinkedList()
        self.cats = LinkedList()

    def add_dog(self, name):
        data = (name, time.time())
        self.dogs.add_last(data)

    def add_cat(self, name):
        data = (name, time.time())
        self.cats.add_last(data)

    def adopt_any(self):
        dog = self.dogs.peek_first()
        cat = self.cats.peek_first()
        if dog[1] < cat[1]:
            return self.adopt_dog()
        else:
            return self.adopt_cat()

    def adopt_dog(self):
        return self.dogs.remove_first()

    def adopt_cat(self):
        return self.cats.remove_first()


if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.init_list([3, 4, 1, 3, 1, 2, 1, 3])
    linkedlist.print_list()
    partition_linked_list(linkedlist, 3).print_list()

    # linkedlist = LinkedList()
    # linkedlist.init_list([2, 4, 1, 3, 1, 2, 1, 3])
    # linkedlist.print_list()
    # print(k2last(linkedlist, 7))

    # linkedlist = LinkedList()
    # linkedlist.init_list([2, 4, 1, 3, 1, 2, 1, 3])
    # linkedlist.print_list()
    # remove_dup(linkedlist).print_list()

    # shelter = AnimalShelter()
    # shelter.add_dog('d1')
    # shelter.add_cat('c1')
    # shelter.add_cat('c2')
    # shelter.add_cat('c3')
    # shelter.add_dog('d2')
    # shelter.add_dog('d3')
    # print(shelter.adopt_cat())
    # print(shelter.adopt_any())
    # print(shelter.adopt_dog())
    # shelter.cats.print_list()
    # shelter.dogs.print_list()
