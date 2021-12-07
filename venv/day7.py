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

def part_1(positions):
    fuel = 99999999999999999999999
    for i in positions:
        fuel_temp = 0
        for j in positions:
            fuel_temp += abs(i-j)
        if fuel_temp<fuel:
            fuel= fuel_temp
    return fuel

def find_fuel_consumption(number):
    return sum(range(1, number+1, 1))

def part_2(positions):
    fuel = 99999999999999999999999
    for i in range(min(positions), round(max(positions)/2)+1):
        fuel_temp = 0
        for j in positions:
            number = abs(i-j)
            fuel_temp += find_fuel_consumption(number)
        if fuel_temp<fuel:
            fuel= fuel_temp
    return fuel


positions = read_file('input_day7.txt')


start_time = time.time()
print('1st part answer: '+ str(part_1(positions)))
print("--- %s seconds for 1st part---" % (time.time() - start_time))


start_time = time.time()
print('2nd part answer: ' + str(part_2(positions)))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
