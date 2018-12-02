# -*- coding: utf8 -*-


from data_structure import Stack


def stack_sort(in_stack):
    """
    3.6, 使用一个额外stack对已有stack进行排序
    :param in_stack:
    :return:
    """
    buffer_stack = Stack([])
    while not in_stack.is_empty():
        var = in_stack.pop()
        if buffer_stack.is_empty() or buffer_stack.peek() < var:
            buffer_stack.push(var)
        else:
            while not buffer_stack.is_empty() and buffer_stack.peek() > var:
                in_stack.push(buffer_stack.pop())
            buffer_stack.push(var)
    return buffer_stack.query()


if __name__ == '__main__':
    print(stack_sort(Stack([1, 5, 2, 4, 3, 6])))
