# -*- coding: utf8 -*-


def unique_characters(string):
    """
    不可以使用additional data structures判断是否是全部unique的string，1.1
    :param string:
    :return:
    """
    if len(string) > 256:
        return False
    record = [False] * 256
    for s in string:
        if record[ord(s)] is True:
            return False
        record[ord(s)] = True
    return True


def is_permutation(s1, s2):
    """
    判断两个字符串是否是排列关系，1.3
    :param s1:
    :param s2:
    :return:
    """
    record = [0] * 256
    for s in s1:
        record[ord(s)] += 1
    for s in s2:
        cur = record[ord(s)]
        if cur < 1:
            return False
        record[ord(s)] -= 1
    if len(set(record)) != 1 or set(record) != {0}:
        return False
    return True


def replace_blank(string, length):
    """
    输入字符串和真实长度，用%20替换空格，不使用额外空间，1.4
    :param string:
    :param length:
    :return:
    """
    record = [''] * length
    cur = -1
    for s in string[::-1]:
        if s != ' ':
            record[cur] = s
            cur -= 1
        else:
            record[cur] = '0'
            record[cur - 1] = '2'
            record[cur - 2] = '%'
            cur -= 3
    return ''.join(record)


def compress_string(string):
    """
    压缩连续重复的字符，如果比之前短则压缩，否则不压缩，1.5
    :param string:
    :return:
    """
    after = _count_compression(string)
    if after >= len(string):
        return string
    new = ''
    last = string[0]
    count = 1
    for s in string[1:]:
        if s == last:
            count += 1
            continue
        else:
            new += f'{last}{count}'
            last = s
            count = 1
    new += f'{last}{count}'
    return new


def _count_compression(string):
    if not string:
        return 0
    size = 0
    count = 1
    last = string[0]
    for s in string[1:]:
        if s == last:
            count += 1
        else:
            size += 1 + len(str(count))
            last = s
            count = 1

    size += 1 + len(str(count))

    return size


def is_prime(num):
    """
    判断一个数是否是质数
    :param num:
    :return:
    """
    from math import sqrt
    if not isinstance(num, int) or num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    # print(unique_characters('helo'))
    # print(is_permutation('hello', 'lohel'))
    # print(replace_blank('good boy go', 15))

    print(_count_compression('hhhhhhhhhhoello'))
    print(compress_string('hhhhhhhhhhoello'))

    # print(is_prime(2))
    # print(is_prime(3))
    # print(is_prime(4))
    # print(is_prime(5 * 7))
    # print(is_prime(5 * 9))
    # print(is_prime(97))
