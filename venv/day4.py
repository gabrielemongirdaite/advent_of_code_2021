import pandas as pd
import numpy as np
import time
from collections import Counter


def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            lines.append(line.split('\n'))
    lines = [i[0] for i in lines if i != ['', ''] ]
    new_list = [lines[i:i + 5] for i in range(1, len(lines), 5)]
    numbers = []
    for i in new_list:
        temp = []
        for j in i:
            temp.append(j.split())
        numbers.append(temp)
    for i in numbers:
        pass
        i.extend([[x,y,z,u,v] for (x, y, z, u, v) in zip(i[0], i[1], i[2], i[3], i[4])])
    return lines[0], numbers

def nested_sum(a) :
    total = 0
    for item in a :
        try:
            total += int(item)
        except TypeError:
            total += nested_sum(item)
    return total

def bingo(numbers, boards):
    for i in list(numbers.split(',')):
        for indx_board, j in enumerate(boards):
            for k in j:
                try:
                    k.remove(i)
                except:
                    pass
                if not any(k):
                    return(nested_sum(boards[indx_board][0:5]*int(i)))

def bingo_all(numbers, boards):
    winners = []
    results = []
    for i in list(numbers.split(',')):
        for indx_board, j in enumerate(boards):
            for k in j:
                try:
                    k.remove(i)
                    if not any(k):
                        if indx_board not in winners:
                            results.append(nested_sum(boards[indx_board][0:5] * int(i)))
                        winners.append(indx_board)
                except:
                    pass
    return results

start_time = time.time()
numbers = read_file("input_day4.txt")[0]
boards = read_file("input_day4.txt")[1]
print('1st part answer: '+ str(bingo(numbers, boards)))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
print('2nd part answer: ' + str(bingo_all(numbers, boards)[-1]))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))


