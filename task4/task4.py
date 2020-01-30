#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

if len(argv) <= 1:
    print('No input file, one data files are required')
else:
    input_data = argv[1]

    with open(input_data, 'r') as list_data:
        list_data = [line.strip().split(' ') for line in list_data]

list_data.sort()
list_start = [i[0].split(':') for i in list_data]
list_end = [i[1].split(':') for i in list_data]


def trans_seconds(list):
    s = []
    for i in list:
        s.append((int(i[0]) - 8) * 60 + int(i[1]))
    return s


list_start_sek = trans_seconds(list_start)
list_end_sek = trans_seconds(list_end)

print(list_data)
print(list_start_sek)
print(list_end_sek)

def has_overlap(A_start, A_end, B_start, B_end):
    latest_start = max(A_start, B_start)
    earliest_end = min(A_end, B_end)
    return (latest_start, earliest_end)

z = list(zip(list_start_sek, list_end_sek))

for i in range(len(z)):
    for f in range(len(z)):
        print(has_overlap(z[i][0], z[i][1], z[f][0], z[f][1]))

'''
noOverlapList = []
start = list_start_sek[0]
end = list_end_sek[0]

for interval in zip(list_start_sek, list_end_sek):
    # if interval overlaps with tempInterval
    if interval[0] < end and interval[1] > end:
        end = interval[1]
    else:
        if interval[0] > end:
            noOverlapList.append((start, end))  # merged non overlapping interval
            start = interval[0]
            end = interval[1]

print(noOverlapList)
# a.start <= b.end AND a.end >= b.start
'''