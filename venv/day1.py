import pandas as pd
import numpy as np
import time


def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            lines.append(int(line))
    return lines

read_file('input_day1.txt')

def count_increases(list_data):
    cnt = 0
    for ind, i in enumerate(list_data[1:]):
        if i>list_data[ind]:
            cnt += 1
    return cnt

def sliding_sum(list_data):
    lst1 = list_data[:len(list_data)-2]
    lst2 = list_data[1:len(list_data)-1]
    lst3 = list_data[2:]

    zipped_lists = zip(lst1, lst2, lst3)
    sum = [x + y + z for (x, y, z) in zipped_lists]
    return sum

start_time = time.time()
print('1st part answer: '+ str(count_increases(read_file("input_day1.txt"))))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
print('2nd part answer: '+ str(count_increases(sliding_sum(read_file("input_day1.txt")))))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))