import numpy as np
import re
import math
import itertools
import time

#number_1 = '[[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]'
#number_2 = '[[[[4,2],2],6],[8,7]]'

def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            line = line.replace('\n', '')
            lines.append(line)
    return lines


def sum_two_smails_numbers(number_1, number_2):
    return '['+number_1+','+number_2+']'

def split_instance(number):
    decoded_str = ''
    for i in number:
        if i.isnumeric():
            decoded_str+='y'
        else:
            decoded_str+='n'
    try:
        answer=decoded_str.index('yy')
    except:
        answer = np.inf
    return answer

def find_number(number, add, start = True):
    try:
        n = re.search(r'\d+', number).group()
        if start:
            return number.replace(n, str(int(n[::-1]) + add)[::-1],1)
        else:
            return number.replace(n, str(int(n) + add), 1)
    except:
        return number


def exploide_instance(number):
    opening = 0
    cnt = 0
    while opening<=4 and cnt <=len(number)-1:
        if number[cnt]=='[':
            opening+=1
        elif number[cnt]==']':
            opening-=1
        cnt += 1
    if cnt == len(number):
        return np.inf
    else:
        return cnt-1


def exploide(number, ind):
    answer = (ind, int(number[ind+1:number.index(',', ind)]), int(number[number.index(',', ind) + 1:number.index(']', ind)]))
    number_start = number[:answer[0]][::-1]
    number_start = find_number(number_start, answer[1])[::-1]
    number = number.replace(number[:answer[0]], number_start, 1)
    number_end = number[number.index(']', ind):]
    number_end = find_number(number_end, answer[2], False)
    number = number.replace(number[number.index(']', ind):], number_end, 1)
    closing_bracket = number.index(']', ind)+1
    number_temp = number[ind:closing_bracket].replace('[' + str(answer[1]) + ',' + str(answer[2]) + ']', '0', 1)
    number = number[:ind]+number_temp+number[closing_bracket:] #number.replace('[' + str(answer[1]) + ',' + str(answer[2]) + ']', '0', 1)
    return number

def split(number, ind):
    n = int(number[ind:ind+2])
    nf = math.floor(n/2)
    nc = math.ceil(n/2)
    number = number.replace(number[ind:ind+2], '['+str(nf)+','+str(nc)+']', 1)
    return number

#sum_snail = sum_two_smails_numbers(number_1, number_2)

def reduce(sum_snail):
    min_exploision = exploide_instance(sum_snail)
    min_split = split_instance(sum_snail)

    while min_exploision!=np.inf:
        sum_snail = exploide(sum_snail, min_exploision)
        min_exploision = exploide_instance(sum_snail)
        min_split = split_instance(sum_snail)
        while min_exploision==np.inf:
            if min_split!=np.inf:
                sum_snail = split(sum_snail, min_split)
                min_exploision = exploide_instance(sum_snail)
                min_split = split_instance(sum_snail)
            else:
                break
    return sum_snail

def magnitude(number):
    try:
        closing = number.index(']')
        opening = number[:closing].rfind('[')
    except:
        closing = -1
    while closing!=-1:
        integers = re.findall(r'\d+', number[opening:closing+1])
        num = int(integers[0])*3+int(integers[1])*2
        number = number[:opening]+str(num)+number[closing+1:]
        try:
            closing = number.index(']')
            opening = number[:closing].rfind('[')
        except:
            closing = -1
    return number


start_time = time.time()
numbers = read_file('input_day18.txt')
sum_snail = numbers[0]
for i in numbers[1:]:
    sum_snail = sum_two_smails_numbers(sum_snail, i)
    sum_snail = reduce(sum_snail)
print('1st part answer: '+ str(magnitude(sum_snail)))
print("--- %s seconds for 1st part---" % (time.time() - start_time))


start_time = time.time()
max_sum_snail = 0
comb = itertools.permutations(numbers,2)

for i in comb:
    sum_snail = sum_two_smails_numbers(i[0], i[1])
    sum_snail = reduce(sum_snail)
    m = int(magnitude(sum_snail))
    max_sum_snail = m if m>max_sum_snail else max_sum_snail
print('2nd part answer: ' + str(max_sum_snail))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))