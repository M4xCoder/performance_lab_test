#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from sys import argv

if len(argv) <= 1:
    print('No input file, data files are required')
else:
    path = argv[1]
    file = ['Cash1.txt', 'Cash2.txt', 'Cash3.txt', 'Cash4.txt', 'Cash5.txt']
    shop = {}
    for name_file in file:
        with open(os.path.join(path, name_file), 'r') as shop_kassa:
            shop[name_file[:-4]] = [float(line.strip()) for line in shop_kassa]

total_kassa= zip(shop.get('Cash1'), shop.get('Cash2'), shop.get('Cash3'), shop.get('Cash4'), shop.get('Cash5'))

max_amount = list(map(sum, total_kassa))

print(max_amount.index(max(max_amount))+1)
