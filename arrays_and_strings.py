# -*- coding: utf8 -*-

from collections import defaultdict
from typing import List


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


def rotate_array(array):
    """
    原位旋转n * n矩阵，1.6
    :param array:
    :return:
    """
    layer = len(array)
    for i in range(layer // 2):
        first = i
        last = layer - 1 - i
        for j in range(first, last):
            offset = j - first
            top = array[first][j]  # 获取顶层元素
            array[first][j] = array[last - offset][first]  # 左侧上移
            array[last - offset][first] = array[last][last - offset]  # 下侧左移
            array[last][last - offset] = array[j][last]  # 右侧下移
            array[j][last] = top  # 上侧右移

    return array


def set_zero(array):
    """
    如果矩阵中有0，则所在行和列都为0，1.7
    :param array:
    :return:
    """
    row, col = [], []
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == 0:
                row.append(i)
                col.append(j)
    for i in range(len(array)):
        for j in range(len(array[0])):
            if i in row or j in col:
                array[i][j] = 0
    return array


def two_sum(nums: list, target: int) -> list:
    """
    leetcode 1
    :param nums:
    :param target:
    :return:
    """
    record = {}
    for i in range(len(nums)):
        if target - nums[i] in record:
            return [record[target - nums[i]], i]
        record[nums[i]] = i
    return []


def sorted_two_sum(numbers: list, target: int) -> list:
    """
    leetcode 167
    :param numbers:
    :param target:
    :return:
    """
    start = 0
    end = len(numbers) - 1
    while start < end:
        current_sum = numbers[start] + numbers[end]
        if current_sum == target:
            return [start + 1, end + 1]
        elif current_sum < target:
            start += 1
        else:
            end -= 1
    return []


class twoSum3:
    """
    Leetcode 170
    """

    def __init__(self):
        self.numbers = defaultdict(int)

    def add(self, number):
        self.numbers[number] += 1

    def find(self, target):
        for one in self.numbers.keys():
            other = target - one
            if other == one and self.numbers[one] < 2:
                continue
            if other not in self.numbers:
                continue
            return True
        return False


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    leetcode 15
    :param nums:
    :return:
    """
    length = len(nums)
    nums.sort()
    response = []
    for i in range(length)[:-2]:
        if i == 0 or nums[i] != nums[i - 1]:
            target = 0 - nums[i]
            start, end = i + 1, length - 1
            while start < end:
                if nums[start] > target // 2 or nums[end] < target // 2:
                    break
                current_sum = nums[start] + nums[end]
                if current_sum == target:
                    response.append([nums[i], nums[start], nums[end]])
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1
                    start += 1
                    end -= 1
                elif current_sum < target:
                    start += 1
                else:
                    end -= 1

    return response


def three_sum_closest(nums: List[int], target: int) -> int:
    """
    leetcode 16
    :param nums:
    :param target:
    :return:
    """
    import sys

    length = len(nums)
    record = [sys.maxsize, 0]
    nums.sort()
    for i in range(length)[:-2]:
        start, end = i + 1, length - 1
        while start < end:
            current_sum = nums[i] + nums[start] + nums[end]
            diff = abs(target - current_sum)
            if diff < record[0]:
                record = [diff, current_sum]
            if current_sum < target:
                start += 1
            else:
                end -= 1
    return record[1]


def three_sum_smaller(nums: List[int], target: int) -> int:
    """
    leetcode 259
    :param nums:
    :param target:
    :return:
    """
    nums.sort()
    count = 0
    length = len(nums)
    for i in range(length)[:-2]:
        if nums[i] >= target:
            break
        left, right = i + 1, length - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum >= target:
                right -= 1
            else:
                count += right - left
                break
    return count


def three_sum_with_multiplicity(nums: List[int], target: int) -> int:
    """
    leetcode 923
    :return:
    """

    def _skip_left(left: int, right: int) -> int:
        while left < right and nums[left] == nums[left + 1]:
            left += 1
        return left

    def _skip_right(left: int, right: int) -> int:
        while left < right and nums[right] == nums[right - 1]:
            right -= 1
        return right

    count = 0
    bound = 10 ** 9 + 7
    record = []
    nums.sort()
    length = len(nums)
    for i in range(length)[:-2]:
        if i == 0 or nums[i] != nums[i - 1]:
            if nums[i] * 3 > target:
                break
            left, right = i + 1, length - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == target:
                    record.append((nums[i], nums[left], nums[right]))
                    left = _skip_left(left, right)
                    right = _skip_right(left, right)
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left = _skip_left(left, right)
                    left += 1
                else:
                    right = _skip_right(left, right)
                    right -= 1
    element = defaultdict(int)
    for e in nums:
        element[e] += 1
    for a, b, c in record:
        if a == b and b == c:
            count = (count + element[a] * (element[a] - 1) * (element[a] - 2) // 6) % bound
        elif a == b:
            count = (count + element[a] * (element[a] - 1) // 2 * element[c]) % bound
        elif b == c:
            count = (count + element[c] * (element[c] - 1) // 2 * element[a]) % bound
        else:
            count = (count + element[a] * element[b] * element[c]) % bound

    return count


if __name__ == '__main__':
    nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    target = 8
    print(three_sum_with_multiplicity(nums, target))
    nums = [1,1,2,2,2,2]
    target = 5
    print(three_sum_with_multiplicity(nums, target))

    # nums = [-2, 0, 1, 3]
    # target = 2
    # print(three_sum_smaller(nums, target))

    # nums = [-1, 2, 1, -4]
    # target = 1
    # print(three_sum_closest(nums, target))

    # two_sum_3 = twoSum3()
    # two_sum_3.add(3)
    # two_sum_3.add(3)
    # print(two_sum_3.find(6))
    # print(two_sum_3.find(4))

    # print(sorted_two_sum([2, 7, 11, 15], 9))
    # print(three_sum([-1, 0, 1, 2, -1, -4]))
    # print(two_sum([2, 7, 11, 15], 9))

    # print(set_zero([[1, 1, 1, 1, 1],
    #                 [2, 2, 0, 2, 2],
    #                 [3, 3, 3, 3, 3],
    #                 [4, 4, 4, 4, 4],
    #                 [5, 5, 5, 5, 5]]))
    # print(rotate_array([[1, 1, 1, 1, 1],
    #                     [2, 2, 2, 2, 2],
    #                     [3, 3, 3, 3, 3],
    #                     [4, 4, 4, 4, 4],
    #                     [5, 5, 5, 5, 5]]))
    # print(unique_characters('helo'))
    # print(is_permutation('hello', 'lohel'))
    # print(replace_blank('good boy go', 15))

    # print(_count_compression('hhhhhhhhhhoello'))
    # print(compress_string('hhhhhhhhhhoello'))

    # print(is_prime(2))
    # print(is_prime(3))
    # print(is_prime(4))
    # print(is_prime(5 * 7))
    # print(is_prime(5 * 9))
    # print(is_prime(97))
