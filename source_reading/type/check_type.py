# -*- coding: utf8 -*-


def list_tuple_check(to_check):
    return isinstance(to_check, (list, tuple))


def none_check(to_check):
    for i in to_check or []:
        print(i)


if __name__ == '__main__':
    print(list_tuple_check([[1, 2], (3, 4)]))
    none_check([1, 2, 3])
    none_check(None)
