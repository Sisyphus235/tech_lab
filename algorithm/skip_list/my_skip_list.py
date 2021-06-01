# -*- coding: utf8 -*-

import random


class SkipListNode:
    def __init__(self, value=None):
        self._value = value
        self._forwards = []  # forward pointers


class SkipList:
    __MAX_LEVEL = 16

    def __init__(self):
        self._level_count = 1
        self._head = SkipListNode()
        self._head._forwards = [None] * self.__MAX_LEVEL  # head of every level

    def __repr__(self):
        ret = ''
        for i in range(self._level_count):
            level_nodes = self._get_level_nodes(i)
            ret += f'level {i}: {level_nodes} \n'

        return ret

    def _get_level_nodes(self, level):
        all_nodes = []
        cur = self._head
        while cur._forwards[level]:
            all_nodes.append(str(cur._forwards[level]._value))
            cur = cur._forwards[level]
        return '->'.join(all_nodes)

    def _random_level(self, p: float = 0.5) -> int:
        level = 1
        while random.random() < p and level < self.__MAX_LEVEL:
            level += 1
        return level

    def insert(self, value):
        level = self._random_level()
        if self._level_count < level:  # update skip list level
            self._level_count = level
        new_node = SkipListNode(value)
        new_node._forwards = [None] * level
        update = [self._head] * level  # a list of prevs in every level of the new node

        p = self._head
        # find the first node that is smaller than the insert value in every level lower than random level
        for i in range(level - 1, -1, -1):
            while p._forwards[i] and p._forwards[i]._value < value:
                p = p._forwards[i]
            update[i] = p  # update prev node in level i

        # insert new node in every level lower than random level
        for i in range(level):
            # similar to
            # new_node.next = prev.next
            # prev.next = new_node
            new_node._forwards[i] = update[i]._forwards[i]
            update[i]._forwards[i] = new_node

    def find_by_value(self, value):
        p = self._head
        for i in range(self._level_count - 1, -1, -1):  # move down a level
            while p._forwards[i] and p._forwards[i]._value < value:
                p = p._forwards[i]  # move along in level i
        return p._forwards[0] if p._forwards[0] and p._forwards[0]._value == value else None

    def delete(self, value):
        update = [None] * self._level_count
        p = self._head
        for i in range(self._level_count - 1, -1, -1):
            while p._forwards[i] and p._forwards[i]._value < value:
                p = p._forwards[i]
            update[i] = p

        if p._forwards[0] and p._forwards[0]._value == value:
            for i in range(self._level_count - 1, -1, -1):
                if update[i]._forwards[i] and update[i]._forwards[i]._value == value:
                    update[i]._forwards[i] = update[i]._forwards[i]._forwards[i]


def test_skip_list():
    skip_list = SkipList()
    skip_list.insert(1)
    skip_list.insert(3)
    skip_list.insert(9)
    skip_list.insert(6)
    skip_list.insert(2)
    print(skip_list)

    assert skip_list.find_by_value(3)._value == 3
    assert skip_list.find_by_value(4) is None

    skip_list.delete(4)
    skip_list.delete(3)
    assert skip_list.find_by_value(3) is None


if __name__ == '__main__':
    test_skip_list()
