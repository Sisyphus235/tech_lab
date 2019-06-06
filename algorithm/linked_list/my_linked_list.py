# -*- coding: utf8 -*-


from typing import Optional


class SingleNode:
    def __init__(self, value: Optional = None):
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next

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
                self.head = SingleNode(value)
                return True
            new_node = SingleNode(value)
            new_node.next = self.head
            self.head = new_node
            return True
        except RuntimeError:
            return False

    def insert_tail(self, value: Optional) -> bool:
        try:
            last_node = self._get_last_node()
            if last_node is None:
                self.head = SingleNode(value)
                return True
            last_node.next = SingleNode(value)
            return True
        except RuntimeError:
            return False

    def delete_head(self) -> bool:
        if self.is_empty:
            return False


def test_single_linked_list():
    single_node = SingleNode(1)
    assert single_node.value == 1
    assert single_node.next is None

    single_linked_list = SingleLinkedList()
    assert single_linked_list.is_empty is True
    single_linked_list.insert_head(1)
    assert single_linked_list.get_all_nodes() == [1]
    single_linked_list.insert_head(2)
    assert single_linked_list.get_all_nodes() == [2, 1]
    single_linked_list.insert_tail(3)
    assert single_linked_list.get_all_nodes() == [2, 1, 3]
    
    for node in single_linked_list:
        print(node)


if __name__ == '__main__':
    test_single_linked_list()
