# -*- coding: utf8 -*-

"""
手中有 n 张牌
第一张放桌上，第二张挪到手牌最下面，第三张放桌上，第四张挪到手牌最下面，
循环直到所有牌都在桌上
如果桌上牌的顺序是 1 - n
原手牌顺序是什么？

i.e.
如果有 5 张牌，桌上顺序是 1，2，3，4，5
手中顺序是 1，5，2，4，3
手中牌流程是：
1 到桌上 5，2，4，3
5 到牌尾 2，4，3，5
2 到桌上 4，3，5
4 到牌尾 3，5，4
3 到桌上 5，4
5 到牌尾 4，5
4 到桌上 5
5 到牌尾 5
5 到桌上
"""

from typing import List


def poker_order(n: int) -> List[int]:
    table = []
    hand = [n for n in range(1, n + 1)]
    count = 0

    while hand:
        if count % 2 == 0:
            table.append(hand.pop(0))
        else:
            hand.append(hand.pop(0))
        count += 1

    ret = [0] * n
    for i, e in enumerate(table):
        ret[e - 1] = i + 1
    print(ret)
    return ret


def test_poker_order():
    assert poker_order(5) == [1, 5, 2, 4, 3]
    assert poker_order(15) == [1, 12, 2, 9, 3, 14, 4, 10, 5, 13, 6, 11, 7, 15, 8]


if __name__ == '__main__':
    test_poker_order()
