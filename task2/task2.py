#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

if len(argv) <= 2:
    print('No input file, two data files are required')
else:
    with open(argv[1], 'r') as input_coordinates:
        coordinates = [line.strip().split(' ') for line in input_coordinates]

    with open(argv[2], 'r') as input_point:
        points = [line.strip().split(' ') for line in input_point]

coordinate_x = []
coordinate_y = []

for coordinate in coordinates:
    coordinate_x.append(float(coordinate[0]))
    coordinate_y.append(float(coordinate[1]))


def in_out(x, y, xp, yp):
    c = 0
    for i in range(len(xp)):
        if (((yp[i] <= y < yp[i - 1]) or (yp[i - 1] <= y < yp[i])) and (
                x > (xp[i - 1] - xp[i]) * (y - yp[i]) / (yp[i - 1] - yp[i]) + xp[i])): c = 1 - c
    return c


def top(x, y, xp, yp):
    for i in range(len(xp)):
        if x == xp[i] and y == yp[i]:
            return 1


def side(x, y, xp, yp):
    list_top = [xy for xy in zip(xp, yp)]
    segment = [list_top[0] + list_top[1],
               list_top[1] + list_top[2],
               list_top[2] + list_top[3],
               list_top[3] + list_top[0],
               ]
    for xy in segment:
        xp1, yp1, xp2, yp2 = xy
        if (xp2 < xp1 and yp1 == yp2) or (yp2 < yp1 and xp1 == xp2):
            xp1, xp2 = xp2, xp1
            yp1, yp2 = yp2, yp1

        if round((x - xp1) * (yp2 - yp1) - (xp2 - xp1) * (y - yp1), 2) == 0 and xp1 <= x <= xp2 and yp1 <= y <= yp2:
            # Точность определения положения точки на ребре завист от кол-ва знаков после запятой.
            return 1


for point in points:
    x = float(point[0])
    y = float(point[1])
    if top(x, y, coordinate_x, coordinate_y) == 1:
        print(0)  # 'Вершина'
    elif side(x, y, coordinate_x, coordinate_y) == 1:
        print(1)  # 'Сторона'
    else:
        if in_out(x, y, coordinate_x, coordinate_y) == 1:
            print(2)  # 'Внутри'
        else:
            print(3)  # 'Снаружи'
