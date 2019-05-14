# -*- coding: utf8 -*-

"""
LBYL means Look Before You Leap
EAFP means Easier to Ask Forgiveness than Permission
"""


def explain(dict_: dict):
    """
    explicit is better than implicit is the principle of Python design
    EAFP is more explicit than LBYL
    with cheap performance cost in python, EAFP is preferable
    reference: https://devblogs.microsoft.com/python/idiomatic-python-eafp-versus-lbyl/
    :param dict_:
    :return:
    """
    # LBYL way
    if "key" in dict_:
        dict_['value'] += 1

    # EAFP way
    try:
        dict_['value'] += 1
    except KeyError:
        pass
