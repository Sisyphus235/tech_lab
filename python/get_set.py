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


class Foo1:
    def __init__(self, x):
        self.x = x

    def __getattribute__(self, item):
        print(f'getattribute called')
        if item == 'x':
            return item
        else:
            raise AttributeError

    def __getattr__(self, item):
        print(f'getattr called')
        return item


class Foo2:
    """
    __set__ and __get__ can avoid inappropriate attribute delete
    """

    def __set__(self, instance, val):
        print(f"Foo2 set called, obj: {instance}, val: {val}")
        instance.x = 2

    def __get__(self, instance, owner):
        print(f"Foo2 get called")
        return instance.x


class Foo3:
    foo2 = Foo2()

    def __init__(self, x):
        self.x = x


class Foo4:
    pass


if __name__ == '__main__':
    """
    ![详细图示](https://hp-markdown-pic.oss-cn-beijing.aliyuncs.com/20190513203254.png)
    https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/
    """
    f1 = Foo1(10)
    print(getattr(f1, 'x'))
    print(getattr(f1, 'y', 'bar'))

    f3 = Foo3(3)
    print(f3.foo2)
    f3.foo2 = 4
    print(f3.foo2)
    del f3.foo2

    # st = Student('a')
    # # a is an attribute of st, so st.a will call __getattibute__ and get 'a' to be printed out
    # print(st.a)
    # # b is not an attribute of st, so st.b will call __getattr__ and b sill be bonded to st, None will be printed out
    # print(st.b)
    # # b is currently an attribute of st, so st,b will call __getattribute__ and get 'student' to be printed out
    # print(st.b)
    #
    # sf = Stuff('a')
    # # sf.a or sf.b will always call __getattribute__ and it doesn't return anything, so None will be printed out
    # print(sf.a)
    # print(sf.b)
    # print(sf.b)
