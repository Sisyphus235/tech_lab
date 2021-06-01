# -*- coding: utf8 -*-

import time
import threading

from contextlib import contextmanager


class LockableArray(list):
    def __init__(self, seq=()):
        super().__init__(seq)
        self._lock = threading.Lock()

    @contextmanager
    def lock(self):
        try:
            result = self._lock.acquire(timeout=1)
            if result:
                yield result
            else:
                raise RuntimeError
        finally:
            self._lock.release()


def lockable_array(array):
    print(f'{threading.current_thread()}')
    try:
        with array.lock():
            print('lock acquired'
                  f'{threading.current_thread()}')
            time.sleep(5)
    except RuntimeError:
        print('lock in use, please wait'
              f'{threading.current_thread()}')


def test_lockable_array():
    array = LockableArray([1])
    for i in range(3):
        t = threading.Thread(target=lockable_array, args=(array,))
        t.start()


if __name__ == '__main__':
    test_lockable_array()
