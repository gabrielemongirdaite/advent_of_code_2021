import pandas as pd
import numpy as np
import time
from collections import Counter


def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            lines.extend(list(line))

    return lines

def recrate_list(lst):
    lst_new = []
    for i in range(0,12):
        lst_tmp = []
        lst_tmp = lst[i::13]
        lst_new.append(lst_tmp)
    return lst_new

def find_bits(lst_new):
    gamma = ''
    epsilon = ''
    for i in lst_new:
        occurence_count = Counter(i)
        gamma += occurence_count.most_common(1)[0][0]
        epsilon += '0' if occurence_count.most_common(1)[0][0]=='1' else '1'
    gamma_int = int(gamma, 2)
    epsilon_int = int(epsilon, 2)
    return gamma_int*epsilon_int

def CO2_generator(lst_new):
    lst_adj = lst_new.copy()
    cnt_bit = 0
    while len(lst_adj[0])>1:
        most_common = '1' if (Counter(lst_adj[cnt_bit]).most_common()[-1][1] == Counter(lst_adj[cnt_bit]).most_common(1)[0][1] and \
                              Counter(lst_adj[cnt_bit]).most_common()[-1][0] != Counter(lst_adj[cnt_bit]).most_common(1)[0][0]) \
            else -1 if (
                    Counter(lst_adj[cnt_bit]).most_common()[-1][1] == Counter(lst_adj[cnt_bit]).most_common(1)[0][1] and \
                    Counter(lst_adj[cnt_bit]).most_common()[-1][0] == Counter(lst_adj[cnt_bit]).most_common(1)[0][0]) \
            else Counter(lst_adj[cnt_bit]).most_common(1)[0][0]
        indices = [i for i, x in enumerate(lst_adj[cnt_bit]) if x == most_common]
        indices.reverse()
        for i in lst_adj:
            for j in indices:
                i.pop(j)
        cnt_bit += 1
    CO2 = ''
    for i in lst_adj:
        CO2 += i[0]
    return int(CO2,2)

def oxygen_generator(lst_new):
    lst_adj = lst_new.copy()
    cnt_bit = 0
    while len(lst_adj[0])>1:
        most_common = '0' if (Counter(lst_adj[cnt_bit]).most_common()[-1][1] == Counter(lst_adj[cnt_bit]).most_common(1)[0][1] and \
                              Counter(lst_adj[cnt_bit]).most_common()[-1][0] != Counter(lst_adj[cnt_bit]).most_common(1)[0][0]) \
            else -1 if (Counter(lst_adj[cnt_bit]).most_common()[-1][1] == Counter(lst_adj[cnt_bit]).most_common(1)[0][1] and \
                              Counter(lst_adj[cnt_bit]).most_common()[-1][0] == Counter(lst_adj[cnt_bit]).most_common(1)[0][0]) \
            else Counter(lst_adj[cnt_bit]).most_common()[-1][0]
        indices = [i for i, x in enumerate(lst_adj[cnt_bit]) if x == most_common]
        indices.reverse()
        for i in lst_adj:
            for j in indices:
                i.pop(j)
        cnt_bit += 1
    oxygen = ''
    for i in lst_adj:
        oxygen += i[0]
    return int(oxygen,2)

start_time = time.time()
print('1st part answer: '+ str(find_bits(recrate_list(read_file('input_day3.txt')))))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
print('2nd part answer: ' + str(CO2_generator(recrate_list(read_file('input_day3.txt')))*oxygen_generator(recrate_list(read_file('input_day3.txt')))))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))