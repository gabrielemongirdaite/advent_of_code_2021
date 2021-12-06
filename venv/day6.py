import pandas as pd
import numpy as np
import time
from collections import Counter


def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            line = line.replace('\n', '')
            line = line.split(',')
            lines.extend(line)
            lines = [int(i) for i in lines]
    return lines

def one_step(initial_state):
    new_state = [number - 1 for number in initial_state]
    try:
        indices = [i for i, x in enumerate(new_state) if x == -1]
        indices.reverse()
        for i in indices:
            new_state[i:i + 1] = (6,8)
    except:
        pass
    return new_state

def create_sequence_of_expansion():
    temp = {-1: 1}
    min_nm = -1
    dct_numbers = {}
    for i in range(0, 40):
        numbers = temp.copy()
        temp = {}
        for i in numbers:
            try:
                temp[i - 7] += 1 * numbers[i]
            except:
                try:
                    temp[i - 7] += 1
                except:
                    temp[i - 7] = 1 * numbers[i]
            try:
                temp[i - 9] += 1 * numbers[i]
            except:
                try:
                    temp[i - 9] += 1
                except:
                    temp[i - 9] = 1 * numbers[i]
        for i in temp:
            try:
                dct_numbers[i] += temp[i]
            except:
                dct_numbers[i] = temp[i]
    return dct_numbers

def find_fish(state, numbers):
    count = 0
    for i in numbers:
        if i>=state:
            count += numbers[i]
    return count+2


start_time = time.time()
initial_state = read_file('input_day6.txt')
state = initial_state
for i in range(0,80):
    state = one_step(state)
print('1st part answer: '+ str(len(state)))
print("--- %s seconds for 1st part---" % (time.time() - start_time))


start_time = time.time()
new_state = [number - 256 for number in initial_state]
cnt = 0
dct_numbers = create_sequence_of_expansion()
for i in new_state:
    cnt += find_fish(i, dct_numbers)
print('2nd part answer: ' + str(cnt))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
