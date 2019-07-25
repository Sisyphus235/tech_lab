# -*- coding: utf8 -*-

import logging

from functools import wraps


def use_logging(func):
    logging.info(f'{func.__name__} is running')
    func()


def foo():
    print(f'this is foo')


def foo2():
    print(f'this is foo2')


def use_logging2(func):
    def wrapper(*args, **kwargs):
        logging.info(f'{func.__name__} is running')
        print(f'use logging2 is working')
        return func(*args, **kwargs)

    return wrapper


@use_logging2
def my_add(a, b):
    print(f'my_add is working, {a} + {b} = {a + b}')


def use_logging3(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == 'info':
                logging.info(f'{func.__name__} is running')
                print('logging info has been recorded.')
            print(f'use logging3 is working in level {level}')
            return func(*args, **kwargs)

        return wrapper

    return decorator


@use_logging3('warn')
def my_minus(a, b):
    print(f'my_minus is working, {a} - {b} = {a - b}')


class Foo:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'class decorator Foo has been called')
        self.func(*args, **kwargs)


@Foo
def bar(a, b, c):
    print(f'bar is working')
    print(f'{a} + {b} - {c} = {a + b - c}')


class Foo2:
    def __init__(self, level):
        self.level = level

    def __call__(self, func, *args, **kwargs):
        def wrapper(*args, **kwargs):
            if self.level == 'info':
                print(f'info log is performed')
            print(f'log info is working on level {self.level}')
            return func(*args, **kwargs)

        return wrapper


@Foo2('info')
def my_mul(a, b):
    print(f'my_mul is working, {a} * {b} = {a * b}')


# examples

# 1.no params in decorator and function
def hello(fn):
    def wrapper():
        print(f"hello, {fn.__name__}")
        fn()
        print(f"goodbye, {fn.__name__}")

    return wrapper


@hello
def greet():
    print("good evening")


# 2.params in decorator
def make_html_tag(tag, *args, **kwargs):
    def real_decorator(fn):
        css_class = f"class={kwargs['css_class'] if 'css_class' in kwargs else ''}"

        def wrapped(*args, **kwargs):
            return f"<{tag} {css_class}> " + fn(*args, **kwargs) + f" </{tag}>"

        return wrapped

    return real_decorator


@make_html_tag(tag="b", css_class="bold_css")
@make_html_tag(tag="i", css_class="italic_css")
def hello():
    return "hello decorator"


# 3.params in function
def memorization(fn):
    cache = {}
    miss = object()

    @wraps(fn)
    def wrapper(*args):
        result = cache.get(args, miss)
        if result is miss:
            result = fn(*args)
            cache[args] = result
        return result

    return wrapper


@memorization
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# 4.class decorator
class MyApp():
    def __init__(self):
        self.func_map = {}

    def register(self, name):
        def func_wrapper(func):
            self.func_map[name] = func
            return func

        return func_wrapper

    def call_method(self, name=None):
        func = self.func_map.get(name, None)
        if func is None:
            raise Exception(f"No function registered against - {name}")
        return func()


if __name__ == '__main__':
    # with use logging module, logging can be handled in one module, but must be modified when adding new functions
    # also, function could not have params
    use_logging(foo)
    use_logging(foo2)

    # with decorator, calling could be done with one line code
    my_add(1, 2)

    # with decorator containing params, complex logic could be handled in decorators
    my_minus(3, 1)

    # function params
    bar(2, 5, 6)

    # decorator params, function params
    my_mul(2, 5)

    greet()
    print(hello())
    print(fib(23))

    app = MyApp()


    @app.register('/')
    def main_page_func():
        return "This is the main page."


    @app.register('/next_page')
    def next_page_func():
        return "This is the next page."


    print(app.call_method('/'))
    print(app.call_method('/next_page'))
