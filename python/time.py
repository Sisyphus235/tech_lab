# -*- coding: utf8 -*-

import time
import datetime

ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S'


def get_utc_time_seconds():
    return datetime.datetime.utcnow().timestamp()


def get_local_time_seconds():
    return time.time()


def seconds2string(seconds):
    return time.ctime(seconds).format(ISOTIMEFORMAT)


if __name__ == '__main__':
    print(get_utc_time_seconds())
    print(get_local_time_seconds())
    print(seconds2string(get_utc_time_seconds()))
    print(seconds2string(get_local_time_seconds()))

    time_since_epoch = time.time()
    print(f'{time_since_epoch} means seconds passed since epoch, with type float')

    print('time.sleep() takes in seconds and suspends the current thread for that long')
    time.sleep(5.3)

    local_time = time.ctime(time_since_epoch)
    print(f'{local_time} means a string representing local time with seconds as input')

    localtime = time.localtime(time_since_epoch)
    print(f'{local_time} means local time with seconds as input')
    utctime = datetime.datetime.utcnow().timestamp()
    print(utctime)
    local_time_utc = time.localtime(utctime)
    print(f'{local_time_utc} means local time with seconds as input')
