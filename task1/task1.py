#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

if len(argv) <= 1:
    print('No input file, one data files are required')
else:
    input_data = argv[1]

    with open(input_data, 'r') as list_data:
        list_data = [float(line.strip()) for line in list_data]


    def median(list_data):
        list_data.sort()
        amount_data = len(list_data)

        if amount_data % 2 == 0:
            median1 = list_data[amount_data // 2]
            median2 = list_data[(amount_data // 2) - 1]
            return (median1 + median2) / 2
        else:
            return list_data[amount_data // 2]


    def percentile(list_data, P):
        list_data.sort()
        amount_data = len(list_data)

        k = (amount_data - 1) * (P / 100) + 1
        per = list_data[int(k) - 1] + k % 1 * (list_data[int(k)] - list_data[int(k) - 1])

        return per


    output_data = [percentile(list_data, 90), median(list_data), max(list_data), min(list_data),
                   sum(list_data) / len(list_data)]

    for line in output_data:
        print(f'{line:.{2}f}')
