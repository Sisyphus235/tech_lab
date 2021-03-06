# -*- coding: utf8 -*-

"""
排序分为两类：内排序和外排序，前者使用内存，后者使用外部存储
"""


# 1.插入排序
## 1.1 直接插入

def pure_insertion(array):
    """
    1.左起为默认值
    2.从第二位循环到最后一位做直接插入
    3.每一位的直接插入是与起左侧比较，停止条件是比左侧大或者到达队列第一位
    :param array:
    :return:
    """
    length = len(array)
    if length <= 1:
        return array
    for i in range(1, length):
        left, cur, index = array[i - 1], array[i], i - 1
        while cur < left:
            array[index], array[index + 1] = array[index + 1], array[index]
            if index == 0:
                break
            left, index = array[index - 1], index - 1
    return array


## 1.2 二分插入

def bisection_insertion(array):
    """
    1.左起为默认值
    2.从第二位循环到最后一位做直接插入
    3.从每一位的左侧通过二分查找找到比他小的值的位置
    4.从当前位置到标记位置依次交换值
    :param array:
    :return:
    """
    length = len(array)
    if length <= 1:
        return array
    for i in range(1, length):
        left, mid, right, temp = 0, 0, i - 1, array[i]
        while left <= right:
            mid = (left + right) // 2
            if temp < array[mid]:
                right = mid - 1
            else:
                left = mid + 1
        for j in range(i, left, -1):
            array[j - 1], array[j] = array[j], array[j - 1]
    return array


## 1.3 希尔插入shell

def shell_insertion(array):
    """

    :param array:
    :return:
    """
    pass


# 2. 选择排序

## 2.1 直接选择排序

## 2.2 堆排序

# 3. 交换排序

## 3.1 冒泡排序

## 3.2 快速排序
def quick_sort_recursive(array: list, left: int, right: int):
    if left < right:
        q = partition(array, left, right)
        quick_sort_recursive(array, left, q - 1)
        quick_sort_recursive(array, q + 1, right)


def partition(array: list, low: int, high: int):
    x = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def findkth(array, left, right, k):
    index = partition(array, left, right)
    if index == k:
        return array[index]
    elif index < k:
        return findkth(array, index + 1, right, k)
    else:
        return findkth(array, left, index - 1, k)


def quick_sort_iterative(array: list):
    left = 0
    right = len(array) - 1
    if left >= right:
        return
    stack = []
    stack.append(left)
    stack.append(right)
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high - low <= 0:
            continue
        x = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        stack.extend([low, i, i + 2, high])


# 4. 归并排序

# 5. 基数排序


if __name__ == '__main__':
    array = [3, 2, 1, 4, 9, 6, 2, 5]
    print(findkth(array, 0, len(array) - 1, 2))
    quick_sort_recursive(array, 0, len(array) - 1)
    print(array)
    # print(quick_sort_iterative([3, 2, 1, 4, 9, 6, 2, 5]))
    # print(pure_insertion([3, 2, 1, 4, 9, 6, 2, 5]))
    # print(pure_insertion([3]))
    # print(bisection_insertion([3, 2, 1, 4, 9, 6, 2, 5]))
