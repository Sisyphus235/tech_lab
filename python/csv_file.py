# -*- coding: utf8 -*-

import csv
import os
from io import StringIO


def write_csv(filename):
    csv_io = StringIO()
    writer = csv.DictWriter(csv_io, fieldnames=['a', '人', 'c'])
    writer.writeheader()

    row = {'a': 1, '人': 2, 'c': 3}
    writer.writerow(row)

    with open(filename, 'w', encoding='utf8') as f:
        f.write(csv_io.getvalue())


def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            print(f'row {i}: {row}')

    with open(filename, 'r') as f:
        dict_reader = csv.DictReader(f)
        print(f'heads: {dict_reader.fieldnames}')
        for i, row in enumerate(dict_reader):
            print(f'row {i + 1}: {row}')


def test_csv():
    filename = 'test.csv'
    write_csv(filename)
    read_csv(filename)
    os.remove(filename)


if __name__ == '__main__':
    test_csv()
