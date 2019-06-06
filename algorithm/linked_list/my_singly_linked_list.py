# -*- coding: utf8 -*-


from typing import Optional


class SinglyNode:
    def __init__(self, value: Optional = None):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next

    def __len__(self):
        return len(self.get_all_nodes)

    def __repr__(self):
        all_nodes = self.get_all_nodes
        return '->'.join(str(node) for node in all_nodes)

    def _get_last_node(self) -> Optional:
        if self.head is None:
            return None
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        return last_node

    @property
    def is_empty(self) -> bool:
        return self.head is None

    @property
    def get_all_nodes(self) -> list:
        all_nodes = []
        cur = self.head
        while cur:
            all_nodes.append(cur.value)
            cur = cur.next
        return all_nodes

    def insert_head(self, value: Optional) -> bool:
        try:
            if self.is_empty:
                self.head = SinglyNode(value)
                return True
            new_node = SinglyNode(value)
            new_node.next = self.head
            self.head = new_node
            return True
        except RuntimeError:
            return False

    def insert_tail(self, value: Optional) -> bool:
        try:
            last_node = self._get_last_node()
            if last_node is None:
                self.head = SinglyNode(value)
                return True
            last_node.next = SinglyNode(value)
            return True
        except RuntimeError:
            return False

    def delete_head(self) -> bool:
        if self.is_empty:
            return False
        self.head = self.head.next
        return True

    def delete_tail(self) -> bool:
        if self.is_empty:
            return False
        if self.head.next is None:
            self.head = None
            return True
        if self.head.next.next is None:
            self.head.next = None
            return True
        cur = self.head
        while cur.next.next:
            cur = cur.next
        cur.next = None
        return True

    def find_by_index(self, index: int) -> SinglyNode:
        cur = self.head
        while cur and index:
            cur = cur.next
            index -= 1
        return cur

    def find_by_value(self, value: Optional) -> SinglyNode:
        cur = self.head
        while cur and cur.value != value:
            cur = cur.next
        return cur


def test_single_linked_list():
    single_node = SinglyNode(1)
    assert single_node.value == 1
    assert single_node.next is None

    single_linked_list = SinglyLinkedList()
    assert single_linked_list.find_by_index(0) is None
    assert single_linked_list.is_empty is True
    print('initialisation', single_linked_list)

    assert single_linked_list.insert_head(1) is True
    assert single_linked_list.get_all_nodes == [1]
    assert single_linked_list.find_by_value(1).value == 1
    assert single_linked_list.find_by_value(2) is None
    print('insert 1: ', single_linked_list)

    assert single_linked_list.insert_head(2) is True
    assert single_linked_list.get_all_nodes == [2, 1]
    print('insert 2 to head: ', single_linked_list)

    assert single_linked_list.insert_tail(3) is True
    assert single_linked_list.get_all_nodes == [2, 1, 3]
    assert len(single_linked_list) == 3
    assert single_linked_list.find_by_index(1).value == 1
    print('insert 3 to tail: ', single_linked_list)

    for node in single_linked_list:
        print(node)

    assert single_linked_list.delete_head() is True
    assert single_linked_list.get_all_nodes == [1, 3]
    print('delete head: ', single_linked_list)

    assert single_linked_list.delete_tail() is True
    assert single_linked_list.get_all_nodes == [1]
    print('delete tail: ', single_linked_list)

    assert single_linked_list.delete_tail() is True
    assert single_linked_list.get_all_nodes == []
    print('delete tail: ', single_linked_list)

    assert single_linked_list.insert_tail(1) is True
    assert single_linked_list.get_all_nodes == [1]
    print('insert 1 to tail: ', single_linked_list)

    assert single_linked_list.delete_head() is True
    assert single_linked_list.get_all_nodes == []
    print('delete head: ', single_linked_list)


if __name__ == '__main__':
    test_single_linked_list()
    """
    链表中环的检测，141
    两个有序链表合并，21
    删除链表倒数第 n 个节点，19
    求链表的中间结点，876
    """
