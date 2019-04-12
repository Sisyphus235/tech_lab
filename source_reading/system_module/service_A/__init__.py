# -*- coding: utf8 -*-

import sys
from types import ModuleType

all_by_module = {
    'service_A.response': ['NotFound', 'Canceled'],
    'service_A.controller': ['foo'],
}

iteritems = lambda d, *args, **kwargs: iter(d.items(*args, **kwargs))

object_origins = {}
for module, items in iteritems(all_by_module):
    for item in items:
        object_origins[item] = module


class MyModule(ModuleType):

    def __getattr__(self, item):
        if item in object_origins:
            module = __import__(object_origins[item], None, None, item)
            for extra_name in all_by_module[module.__name__]:
                setattr(self, extra_name, getattr(module, extra_name))
            return getattr(module, item)
        return ModuleType.__getattribute__(self, item)


sys.modules['my_module'] = MyModule('my_module')
