# -*- coding: utf8 -*-

from functools import wraps


def singleton1(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]

    return inner


def singleton2(cls):
    _instance = {}

    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kw)
        return _instance[cls]

    return getinstance


class Singleton1:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton1, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Singleton2:
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]
