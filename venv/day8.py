import pandas as pd
import numpy as np
import time
from collections import Counter


def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            line = line.replace('\n', '')
            line = line.split(' | ')
            lines.append(line)
    return lines

def easy_digits(entries):
    cnt = 0
    for i in entries:
        for j in i[1].split(' '):
            if len(j) in [2, 3, 4, 7]:
                cnt += 1
    return cnt

def c_f(entry):
    cf = []
    for i in entry[0].split(' '):
        if len(i)==2:
            cf.extend(i)
    return (cf[0], cf[1])

def a(entry):
    cf = c_f(entry)
    for i in entry[0].split(' '):
        if len(i)==3:
            seven = i
    for i in cf:
        seven = seven.replace(i,'')
    return seven

def c_e_d(entry):
    ced = []
    zero_nine = []
    cf = c_f(entry)
    for i in entry[0].split(' '):
        if len(i) == 6:
            ced.append(i)
            if  cf[0]  in i and cf[1]  in i:
                zero_nine.append(i)
    for i in ced:
        if i not in zero_nine:
            six = i
    return ((list(set(ced[0]) - set(ced[1]))[0], list(set(ced[1]) - set(ced[0]))[0], list(set(ced[1]) - set(ced[2]))[0]), six, zero_nine)

def c(entry):
    six = c_e_d(entry)[1]
    cf = c_f(entry)
    return list(set(cf)-set(six))[0]

def f(entry):
    c_val = c(entry)
    cf = c_f(entry)
    return list(set(cf) - set(c_val))[0]

def d_g(entry):
    a_value = a(entry)
    adg = []
    for i in entry[0].split(' '):
        if len(i) == 5:
            adg.append(i)
    adg_values = set(adg[0]).intersection(adg[1]).intersection(adg[2])
    return list(adg_values - set(a_value))

def g(entry):
    dg = d_g(entry)
    for i in entry[0].split(' '):
        if len(i) == 4:
            four = i
    return list(set(dg) - set(four))

def d(entry):
    g_value = g(entry)
    dg = d_g(entry)
    return list(set(dg) - set(g_value))

def b_e(entry):
    zero_nine = c_e_d(entry)[2]
    a_value = a(entry)[0]
    c_value = c(entry)[0]
    d_value = d(entry)[0]
    f_value = f(entry)[0]
    g_value = g(entry)[0]
    for i in zero_nine:
        if d_value in i:
            nine = i
    b_value = list(set(nine)-{a_value, c_value, d_value, f_value, g_value})[0]
    e_value = list({'a', 'b', 'c', 'd', 'e', 'f', 'g'}-{a_value, b_value, c_value, d_value, f_value, g_value})[0]
    return (b_value, e_value)

def number_template(str):
    if str == 'cf':
        return 1
    elif str == 'acdeg':
        return 2
    elif str == 'acdfg':
        return 3
    elif str == 'bcdf':
        return 4
    elif str == 'abdfg':
        return 5
    elif str =='abdefg':
        return 6
    elif str =='acf':
        return 7
    elif str =='abcdfg':
        return 9
    elif str=='abcdefg':
        return 8
    elif str=='abcefg':
        return 0
    else:
        return 100000

def find_number(entry):
    map = [('a', a(entry)[0]), ('b', b_e(entry)[0]), ('c', c(entry)[0]), ('d', d(entry)[0]), ('e', b_e(entry)[1]), ('f', f(entry)[0]), ('g', g(entry)[0])]
    sorted_list = []
    number = 0
    for ind, i in enumerate(entry[1].split(' ')):
        i_temp = ''
        for ind2, k in enumerate(i):
            for j in map:
                if k==j[1]:
                    i_temp += k.replace(j[1], j[0])
        if ind == 0:
            number += number_template(''.join(sorted(i_temp)))*1000
        elif ind==1:
            number += number_template(''.join(sorted(i_temp))) * 100
        elif ind==2:
            number += number_template(''.join(sorted(i_temp))) * 10
        else:
            number += number_template(''.join(sorted(i_temp)))
    return number


entry = read_file('input_day8.txt')
print(easy_digits(entry))
# one_entry = ['gcfabe gbdc bgdacfe gbecdf ebgfc bcdfe dc degfca ced befad', 'bdgfeca dceagf cefdga ebdfa']
# print(find_number(one_entry))
number = 0
for i in entry:
    number +=find_number(i)

print(number)