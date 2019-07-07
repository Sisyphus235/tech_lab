# -*- coding: utf8 -*-

"""
完成一个 lru cache 的装饰器，传入空间 size 和运行值，实现 lru 缓存功能
"""


class LruCache:
    def __init__(self, size=0):
        self.capacity = size
        self.pointer = 0
        self.space = [None] * size
        self.value = [None] * size

    def __call__(self, func, *args):
        print(f'lru called \nsize is {self.capacity} \nspace is {self.space}\n')

        def wrapper(*args):
            key = hash(args)
            val = self.space_search(key)
            if val:
                return val
            print(f'new calculation performed')
            ret = func(*args)
            self.space_set(key, ret)
            return ret

        return wrapper

    def space_search(self, key):
        for i in range(self.pointer):
            if self.space[i] == key:
                ret = self.value[i]
                print(f'result is cached on position {i}, space is {self.space}, value is {self.value}')
                for j in range(i, 0, -1):
                    self.space[j], self.space[j - 1] = self.space[j - 1], self.space[j]
                    self.value[j], self.value[j - 1] = self.value[j - 1], self.value[j]
                print(f'new space and value is\n{self.space}\n{self.value}\n')
                return ret
        return None

    def space_set(self, key, value):
        tmp_key = key
        tmp_val = value
        for i in range(self.pointer + 1):
            next_key = self.space[i]
            self.space[i] = tmp_key
            tmp_key = next_key

            next_val = self.value[i]
            self.value[i] = tmp_val
            tmp_val = next_val
        if self.pointer != self.capacity - 1:
            self.space[self.pointer] = tmp_key
            self.value[self.pointer] = tmp_val
            self.pointer += 1
        print(f'new cache added, new space and value is\n{self.space}\n{self.value}\npointer is {self.pointer}\n')


@LruCache(2)
def my_add(a, b):
    return a + b


def test_lru_cache():
    my_add(1, 2)
    my_add(1, 2)
    my_add(3, 2)
    my_add(3, 2)
    my_add(1, 2)


if __name__ == '__main__':
    test_lru_cache()
