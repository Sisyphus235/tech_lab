# -*- coding: utf8 -*-


class Foo:
    pass


class Meta(type):
    pass


class MetaFoo(metaclass=Meta):
    pass


if __name__ == '__main__':
    # custom class is the instance of type
    foo = Foo()
    print(isinstance(foo, Foo))
    print(isinstance(Foo, type))
    print(type(foo))

    # make a class directly using type, without class statement
    MyClass = type('MyClass', (), {})
    my_class = MyClass()
    print(isinstance(my_class, MyClass))
    print(isinstance(MyClass, type))
    print(type(my_class))

    # make a custom metaclass
    print(type(MetaFoo))
