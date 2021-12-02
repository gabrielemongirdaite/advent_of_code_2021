import pandas as pd
import numpy as np
import time


def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            lines.append((line.split()))
        for i in lines:
            i[1]=int(i[1])
    return lines

def find_position(lst):
    horizontal = 0
    depth = 0
    for i in lst:
        if i[0]=='forward':
            horizontal+= i[1]
        elif i[0]=='down':
            depth += i[1]
        else:
            depth -= i[1]
    return depth*horizontal

def find_position_with_aim(lst):
    horizontal = 0
    depth = 0
    aim = 0
    for i in lst:
        if i[0]=='forward':
            horizontal+= i[1]
            depth += aim*i[1]
        elif i[0]=='down':
            aim += i[1]
        else:
            aim -= i[1]
    return depth*horizontal

start_time = time.time()
print('1st part answer: '+ str(find_position(read_file("input_day2.txt"))))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
print('2nd part answer: '+ str(find_position_with_aim(read_file("input_day2.txt"))))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))