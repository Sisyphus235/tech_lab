# -*- coding: utf8 -*-

import os
import types


def file_open(root_path, filename):
    # use os.path.join to concatenate directory and filename
    filename = os.path.join(root_path, filename)
    d = types.ModuleType('file')
    d.__file__ = filename

    try:
        with open(filename, 'r') as file:
            for line in file.readlines():
                print(line)
            exec(compile(file.read(), filename, 'exec'), d.__dict__)
    except IOError as e:
        # IOError 报错时的提示信息
        e.strerror = "file open error testing"
        print(f'e: {e}')
        raise


if __name__ == '__main__':
    file_open('/Users/hongfu/Work/Computer_science/tech_lab', 'singleton.ply')
