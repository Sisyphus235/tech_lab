# -*- coding: utf8 -*-

from functools import wraps


class MySingleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance


class MyLazySingleton:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = MyLazySingleton()
        return cls.instance


def function_singleton_decorator(cls):
    _instance = dict()

    @wraps(cls)
    def inner(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return inner


def test_singleton():
    # test normal class
    class Foo:
        def __init__(self):
            pass

    f1 = Foo()
    f2 = Foo()
    assert id(f1) != id(f2)

    # test singleton
    s1 = MySingleton()
    s2 = MySingleton()
    assert id(s1) == id(s2)

    # test lazy singleton
    s1 = MyLazySingleton()
    s2 = MyLazySingleton()
    assert id(s1.get_instance()) == id(s2.get_instance())

    # test functional singleton decorator
    @function_singleton_decorator
    class TestFunctionSingletonDecorator:
        def __init__(self, val):
            self.val = val
            print(f'the id of function is {id(self)}')

    a = TestFunctionSingletonDecorator(1)
    b = TestFunctionSingletonDecorator(2)
    assert a.val == b.val


if __name__ == '__main__':
    test_singleton()
