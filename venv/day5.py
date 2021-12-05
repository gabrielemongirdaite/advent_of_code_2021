import pandas as pd
import numpy as np
import time
from collections import Counter


def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            line = line.replace('\n', '').split(' -> ')
            start = line[0].split(',')
            end  = line[1].split(',')
            coordinates = [(int(start[0]), int(start[1])), (int(end[0]), int(end[1]))]
            lines.append(coordinates)
    return lines

def horizontal_vertical_coordinates(coordinates):
    relevant_coordinates = []
    for i in coordinates:
        if i[0][0]==i[1][0] or i[0][1]==i[1][1]:
            relevant_coordinates.append(i)
    return relevant_coordinates

def points(coordinates):
    all_points = []
    for i in coordinates:
        if i[0][0] == i[1][0] or i[0][1] == i[1][1]:
            for x in range(min(i[0][0], i[1][0]), max(i[0][0], i[1][0])+1):
                for y in range(min(i[0][1], i[1][1]), max(i[0][1], i[1][1])+1):
                    all_points.append((x,y))
        else:
            x1 = i[0][0]
            y1 = i[0][1]
            x2 = i[1][0]
            y2 = i[1][1]
            all_points.append((x2, y2))
            increase_x = 1 if x1>x2 else -1
            increase_y = 1 if y1>y2 else -1
            while x1!=x2 and y1!=y2:
                x2 += increase_x
                y2 += increase_y
                all_points.append((x2, y2))
    return all_points

def overlap(points):
    occurences = Counter(points)
    cnt = 0
    for i in occurences:
        if occurences[i]>1:
            cnt+=1
    return cnt


start_time = time.time()
coordinates = read_file('input_day5.txt')
relevant_coordinates = horizontal_vertical_coordinates(coordinates)
points_hor_ver = points(relevant_coordinates)
print('1st part answer: '+ str(overlap(points_hor_ver)))
print("--- %s seconds for 1st part---" % (time.time() - start_time))


start_time = time.time()
points_all = points(coordinates)
print('2nd part answer: ' + str(overlap(points_all)))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
