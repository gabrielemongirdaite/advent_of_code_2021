import pandas as pd
import numpy as np
import time


def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            line = line.replace('\n', '')
            ln = []
            for j in line:
                ln.extend(j)
            ln = [int(i) for i in ln]
            lines.append(ln)
    return lines

def above_dir(x,y):
    if x - 1 >= 0:
        above = seq[x - 1][y]
    else:
        above = 9
    return above

def below_dir(x,y):
    try:
        below = seq[x + 1][y]
    except:
        below = 9
    return below

def left_dir(x,y):
    if y - 1 >= 0:
        left = seq[x][y - 1]
    else:
        left = 9
    return left

def right_dir(x,y):
    try:
        right = seq[x][y + 1]
    except:
        right = 9
    return right

def low_points(seq):
    s = 0
    coordinates = []
    for x, i in enumerate(seq):
        for y, j in enumerate(i):
            above = above_dir(x,y)
            left = left_dir(x,y)
            below = below_dir(x,y)
            right = right_dir(x,y)
            if above > j and left > j and below > j and right > j:
                s += j+1
                coordinates.append((x,y))
    return s, coordinates

def going_up(x,y,seq, all_points_full):
    cnt = 0
    point = seq[x][y]
    new_points = []
    while point != 9:
        point = above_dir(x, y)
        x = x - 1
        if point!=9 and (x,y) not in all_points_full:
            new_points.extend([(x,y)])
            cnt += 1
    return cnt, new_points

def going_left(x,y,seq, all_points_full):
    cnt = 0
    point = seq[x][y]
    new_points = []
    while point != 9:
        point = left_dir(x, y)
        y = y - 1
        if point!=9 and (x,y) not in all_points_full:
            new_points.extend([(x,y)])
            cnt += 1
    return cnt, new_points

def going_down(x,y,seq, all_points_full):
    cnt = 0
    point = seq[x][y]
    new_points = []
    while point != 9:
        point = below_dir(x, y)
        x = x +1
        if point!=9 and (x,y) not in all_points_full:
            new_points.extend([(x,y)])
            cnt += 1
    return cnt, new_points

def going_right(x,y,seq, all_points_full):
    cnt = 0
    point = seq[x][y]
    new_points = []
    while point != 9:
        point = right_dir(x, y)
        y = y+1
        if point!=9 and (x,y) not in all_points_full:
            new_points.extend([(x,y)])
            cnt += 1
    return cnt, new_points

def basins(low_points_ccordinates, seq):
    basin_size = []
    for i in low_points_ccordinates:
        all_points = [(i[0], i[1])]
        all_points_full = [(i[0], i[1])]
        cnt = 0
        while all_points!=[]:
            tmp = []
            for j in all_points:
                add, new_points = going_up(j[0], j[1], seq, all_points_full)
                cnt += add
                tmp.extend(new_points)
                all_points_full.extend(new_points)

                add, new_points = going_left(j[0], j[1], seq, all_points_full)
                cnt += add
                tmp.extend(new_points)
                all_points_full.extend(new_points)

                add, new_points = going_down(j[0], j[1], seq, all_points_full)
                cnt += add
                tmp.extend(new_points)
                all_points_full.extend(new_points)

                add, new_points = going_right(j[0], j[1], seq, all_points_full)
                cnt += add
                tmp.extend(new_points)
                all_points_full.extend(new_points)

                all_points.remove(j)
            all_points.extend(tmp)
        basin_size.append(cnt+1)
    return basin_size

seq = read_file('input_day9.txt')



start_time = time.time()
low_points, coordinates = low_points(seq)
print('1st part answer: '+ str(low_points))
print("--- %s seconds for 1st part---" % (time.time() - start_time))


start_time = time.time()
basins_size = basins(coordinates, seq)
basins_size.sort()
print('2nd part answer: ' + str(np.prod(basins_size[-3:])))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
