# -*- coding: utf8 -*-


class TypeConversionDict(dict):
    def get(self, key, default=None, type=None):
        """Return the default value if the requested data doesn't exist.
        If `type` is provided and is a callable it should convert the value,
        return it or raise a :exc:`ValueError` if that is not possible.  In
        this case the function will return the default as if the value was not
        found:

        >>> d = TypeConversionDict(foo='42', bar='blub')
        >>> d.get('foo', type=int)
        42
        >>> d.get('bar', -1, type=int)
        -1

        :param key: The key to be looked up.
        :param default: The default value to be returned if the key can't
                        be looked up.  If not further specified `None` is
                        returned.
        :param type: A callable that is used to cast the value in the
                     :class:`MultiDict`.  If a :exc:`ValueError` is raised
                     by this callable the default value is returned.
        """
        try:
            rv = self[key]
        except KeyError:
            return default

        if type is not None:
            try:
                rv = type(rv)
            except ValueError:
                rv = default

        return rv


if __name__ == '__main__':
    type_conversion_dict = TypeConversionDict(a=1, b=2)
    print(type_conversion_dict.get('a'))
    print(type_conversion_dict.get('a', type=bool))
    print(type_conversion_dict.get('c'))
    print(type_conversion_dict.get('c', 3))
    print(type_conversion_dict.get('c', 3, type=bool))
