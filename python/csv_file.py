# -*- coding: utf8 -*-

import csv
import os
from io import StringIO


def write_file(filename):
    csv_io = StringIO()
    writer = csv.DictWriter(csv_io, fieldnames=['a', 'b', 'c'])
    writer.writeheader()

    row = [1, 2, 3]
    writer.writerow(row)

    with open(filename, 'w') as f:
        f.write(csv_io.getvalue())


def test_csv():
    filename = 'test.csv'
    write_file(filename)

    os.remove(filename)


if __name__ == '__main__':
    test_csv()
