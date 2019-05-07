# -*- coding: utf8 -*-


def list_tuple_check(to_check):
    return isinstance(to_check, (list, tuple))


if __name__ == '__main__':
    print(list_tuple_check([(1, 2)]))
