# -*- coding: utf8 -*-


class Foo:
    def __init__(self, *, a, b):
        self.a = a
        self.b = b


def get_env_var():
    import os
    return os.environ.get('PYENV_VERSION')


if __name__ == '__main__':
    f = Foo(a=1, b=2)
    print(f.a, f.b)

    try:
        f = Foo(1, 2)
    except TypeError:
        print("params should be in key value pair")

    print(get_env_var())
