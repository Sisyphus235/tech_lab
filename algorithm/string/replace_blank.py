# -*- coding: utf8 -*-

"""
将输入字符串种的每个空格替换为 "%20"
例如，
输入 "we are happy"
输出 "we%20are%20happy"
"""


def replace_blank(s: str) -> str:
    length = 0
    for e in s:
        if e == ' ':
            length += 3
        else:
            length += 1

    if length == 0:
        return ''

    point = length - 1
    array = [' '] * length
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ' ':
            array[point] = '0'
            array[point - 1] = '2'
            array[point - 2] = '%'
            point -= 3
        else:
            array[point] = s[i]
            point -= 1

    return ''.join(array)


def test_replace_blank():
    s = 'we are happy'
    assert replace_blank(s) == 'we%20are%20happy'
    s = ' '
    assert replace_blank(s) == '%20'
    s = ' test  '
    assert replace_blank(s) == '%20test%20%20'
    s = 'new'
    assert replace_blank(s) == 'new'
    s = ''
    assert replace_blank(s) == ''


if __name__ == '__main__':
    test_replace_blank()
