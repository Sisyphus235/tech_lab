# -*- coding: utf8 -*-


class Student:
    def __init__(self, a):
        self.a = a

    def __getattr__(self, item):
        setattr(self, item, "student")


class Stuff:
    def __init__(self, a):
        self.a = a

    def __getattribute__(self, item):
        setattr(self, item, "stuff")


if __name__ == '__main__':
    st = Student('a')
    # a is an attribute of st, so st.a will call __getattibute__ and get 'a' to be printed out
    print(st.a)

    sf = Stuff('a')
    # sf.a will call __getattribute__ and it doesn't return anything, so None will be printed out
    print(sf.a)
