# -*- coding: utf8 -*-


def hanoi_move(num, start, buffer, end):
    """
    Hanoi move汉诺塔移动
    :param num:
    :param start:
    :param buffer:
    :param end:
    :return:
    """
    count = 0
    if num == 1:
        print(f'move from plate {start} to plate {end}')
        return 1
    count += hanoi_move(num - 1, start, end, buffer)
    count += hanoi_move(1, start, buffer, end)
    count += hanoi_move(num - 1, buffer, start, end)
    return count


if __name__ == '__main__':
    print(hanoi_move(3, 'a', 'b', 'c'))
