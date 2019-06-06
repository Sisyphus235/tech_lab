# -*- coding: utf8 -*-


import time
from data_structure import LinkedList, LinkedListNode


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


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    l = ListNode(-1)
    head = l
    carry = 0

    while l1 or l2 or carry:
        total, carry = carry, 0
        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next
        if total > 9:
            total -= 10
            carry = 1
        l.next = ListNode(total)
        l = l.next

    return head.next


def add_two_numbers_II(l1: ListNode, l2: ListNode) -> ListNode:
    l1_stack = []
    while l1:
        l1_stack.append(l1.val)
        l1 = l1.next
    l2_stack = []
    while l2:
        l2_stack.append(l2.val)
        l2 = l2.next

    carry = 0
    head = None
    while l1_stack or l2_stack or carry:
        total, carry = carry, 0
        if l1_stack:
            total += l1_stack.pop()
        if l2_stack:
            total += l2_stack.pop()
        if total > 9:
            total -= 10
            carry = 1
        cur = ListNode(total)
        cur.next = head
        head = cur

    return head


def linked_list_sum1(l1, l2):
    """
    计算两个单向链表的加和，个位在前，2.5
    :param l1:
    :param l2:
    :return:
    """
    result = LinkedList()
    buff = 0
    cur_l1 = l1.head
    cur_l2 = l2.head
    while cur_l1 or cur_l2:
        v1, v2 = 0, 0
        if cur_l1:
            v1 = cur_l1.val
        if cur_l2:
            v2 = cur_l2.val
        total = v1 + v2 + buff
        if total > 9:
            buff = 1
            total -= 10
        else:
            buff = 0
        result.add_last(total)
        if cur_l1:
            cur_l1 = cur_l1.next
        if cur_l2:
            cur_l2 = cur_l2.next
    return result


def linked_list_sum2(l1, l2):
    """
    计算两个单向链表的加和，个位在后，2.5
    :param l1:
    :param l2:
    :return:
    """
    # filter input
    count = 0
    point1, point2 = l1.head, l2.head
    if not point2 and not point1:
        return
    if not point1:
        return l2
    if not point2:
        return l1

    # padding shorter list
    shorter = None
    while point1 or point2:
        if point1 and point2:
            point1 = point1.next
            point2 = point2.next
            continue
        count += 1
        point1 = point1.next if point1 else None
        point2 = point2.next if point2 else None
        if shorter:
            continue
        elif point1:
            shorter = l2
        else:
            shorter = l1

    if shorter:
        while count != 0:
            zero = LinkedListNode(0)
            zero.next = shorter.head
            shorter.head = zero
            count -= 1

    # linklists add
    rsp = LinkedList()
    rsp.init_list([0])
    rsp_point = rsp.head
    point1, point2 = l1.head, l2.head
    total = point1.val + point2.val
    if total > 9:
        rsp.head.val = 1
        rsp.head.next = LinkedListNode(total - 10)
    else:
        rsp.head.next = LinkedListNode(total)

    rsp_point = rsp_point.next

    while point1.next:
        total = point1.next.val + point2.next.val
        if total > 9:
            rsp_point.next = LinkedListNode(total - 10)
            rsp_point.val += 1
        else:
            rsp_point.next = LinkedListNode(total)
        point1 = point1.next
        point2 = point2.next
        rsp_point = rsp_point.next

    # trim rsp
    point = rsp.head
    update = []
    while point:
        if point.val < 10:
            flag = True if point.val == 9 else False
            update.append([0, flag])
        else:
            flag = False
            point.val -= 10
            update.append([0, flag])
            start = -2
            while update[start][1] and abs(start) <= len(update):
                update[start][0] += 1
                update[start][1] = False
                start -= 1
            update[start][0] += 1
        point = point.next

    count = 0
    point = rsp.head
    while point:
        point.val += update[count][0]
        if point.val > 9:
            point.val -= 10
        count += 1
        point = point.next

    return rsp


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


def sort_linked_list(linked_list: LinkedList) -> LinkedList:
    """
    奇数节点升序，偶数节点降序，返回升序链表
    解法：1.生成奇偶两个新链表；2.偶数链表反转；3.奇偶链表合并新链表
    :param linked_list:
    :return:
    """
    left_list = LinkedList()
    right_list = LinkedList()
    cur = linked_list.head
    i = 0
    while cur:
        i += 1
        if i % 2:
            left_list.add_last(cur.val)
        else:
            right_list.add_last(cur.val)
        cur = cur.next
    right_list = reverse_linked_list(right_list)
    left_pointer = left_list.head
    right_pointer = right_list.head
    merge_list = LinkedList()
    while left_pointer or right_pointer:
        if left_pointer and right_pointer:
            if left_pointer.val <= right_pointer.val:
                merge_list.add_last(left_pointer.val)
                left_pointer = left_pointer.next
            else:
                merge_list.add_last(right_pointer.val)
                right_pointer = right_pointer.next
        elif left_pointer:
            merge_list.add_last(left_pointer.val)
            left_pointer = left_pointer.next
        else:
            merge_list.add_last(right_pointer.val)
            right_pointer = right_pointer.next
    return merge_list


if __name__ == '__main__':
    l1 = ListNode(7)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l1.next.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    l = add_two_numbers_II(l1, l2)
    print(l.val, l.next.val, l.next.next.val, l.next.next.next.val)

    # l = LinkedList()
    # l.init_list([1, 7, 2, 6, 7, 2, 11])
    # l.print_list()
    # sort = sort_linked_list(l)
    # sort.print_list()
    # l = LinkedList()
    # l.init_list([1, 2, 3, 4, 5])
    # l.print_list()
    # revert = reverse_linked_list(l)
    # revert.print_list()

    # l1 = LinkedList()
    # l1.init_list([1, 2, 3, 4])
    # l2 = LinkedList()
    # l2.init_list([3, 8, 7, 6, 6])
    # linked_list_sum2(l1, l2).print_list()
    #
    # l1 = LinkedList()
    # l1.init_list([2, 7, 4])
    # l2 = LinkedList()
    # l2.init_list([9, 2, 1, 7, 9])
    # linked_list_sum2(l1, l2).print_list()

    # linked_list_sum1(l1, l2).print_list()

    # linkedlist = LinkedList()
    # linkedlist.init_list([3, 4, 1, 3, 1, 2, 1, 3])
    # linkedlist.print_list()
    # partition_linked_list(linkedlist, 3).print_list()

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
