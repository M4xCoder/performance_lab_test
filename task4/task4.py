#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from collections import defaultdict
from itertools import groupby, tee
import datetime

if len(argv) <= 1:
    print('No input file, one data files are required')
else:
    input_data = argv[1]

    with open(input_data, 'r') as list_data:
        list_data = [line.strip().split(' ') for line in list_data]

list_data.sort()
list_start = [i[0].split(':') for i in list_data]
list_end = [i[1].split(':') for i in list_data]


def trans_minutes(list):
    s = []
    for i in list:
        s.append((int(i[0]) - 8) * 60 + int(i[1]))
    return s


list_start_minute = trans_minutes(list_start)
list_end_minute = trans_minutes(list_end)
list_data_minute = list(zip(list_start_minute, list_end_minute))

spisok = []
amount = 0
for i in range(480):
    for poset in list_data_minute:
        if poset[0] <= i < poset[1]:
            amount += 1
    spisok.append(amount)
    amount = 0


def list_duplicates(seq):
    tally = defaultdict(list)
    for i, item in enumerate(seq):
        tally[item].append(i)
    return ((key, locs) for key, locs in tally.items()
            if len(locs) > 1)


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def grouper_periods(lst):
    result = []
    for k, g in groupby(pairwise(lst), key=lambda x: x[1] - x[0]):
        g = list(g)
        if len(g) > 1:
            try:
                if g[0][0] == result[-1]:
                    del result[-1]
                elif g[0][0] == result[-1][1]:
                    g = g[1:]  # patch for duplicate start and/or end
            except (IndexError, TypeError):
                pass
            result.append((g[0][0], g[-1][-1], k))
        else:
            result.append(g[0][-1]) if result else result.append(g[0])
    return result


periods = grouper_periods(max(list(list_duplicates(spisok)))[1])


def convert(n):
    return str(datetime.timedelta(minutes=n) + datetime.timedelta(hours=8))


for i in periods:
    start = convert(i[0])
    end = convert(i[1] + i[2])
    print(start[:-3], end[:-3])
