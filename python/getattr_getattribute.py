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
    # b is not an attribute of st, so st.b will call __getattr__ and b sill be bonded to st, None will be printed out
    print(st.b)
    # b is currently an attribute of st, so st,b will call __getattribute__ and get 'student' to be printed out
    print(st.b)

    sf = Stuff('a')
    # sf.a or sf.b will always call __getattribute__ and it doesn't return anything, so None will be printed out
    print(sf.a)
    print(sf.b)
    print(sf.b)
