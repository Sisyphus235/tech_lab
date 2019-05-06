# -*- coding: utf8 -*-

"""
Existing uses include:

In slice syntax to represent the full slice in remaining dimensions
In type hinting to indicate only part of a type(Callable[..., int] or Tuple[str, ...])
In type stub files to indicate there is a default value without specifying it

Possible uses could include:

As a default value for places where None is a valid option
As the content for a function you haven't implemented yet
"""


class Structure:
    pre_defined = [Ellipsis, Ellipsis]
    placeholder = ...

    def __getitem__(self, item):
        return item

    def get_structure(self, silent=False):
        if self.pre_defined[silent] is not Ellipsis:
            return self.pre_defined[silent]
        return Ellipsis

    def set_structure(self, *args):
        self.pre_defined = args[0], args[1]


if __name__ == '__main__':
    s = Structure()
    print(s.get_structure())

    s.set_structure(0, 1)
    print(s.get_structure())

    assert s[...] is Ellipsis
    assert s.placeholder is Ellipsis
