import re
import collections
import itertools


def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            line = line.replace('\n', '')
            line = line.split(' ')
            ln = []
            ln.append(line[0])
            line1 = line[1].split(',')
            num = []
            for i in line1:
                num.extend(re.findall(r'-?\d+', i))
            ln.append((int(num[0]), int(num[1]) ))
            ln.append((int(num[2]), int(num[3]) ))
            ln.append((int(num[4]), int(num[5]) ))
            lines.append(ln)
            # lines.append(line)
    return lines

def read_file2(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            line = line.replace('\n', '')
            line = line.split(' ')
            ln = []
            ln.append(line[0])
            line1 = line[1].split(',')
            num = []
            for i in line1:
                num.extend(re.findall(r'-?\d+', i))
            ln.append(range(int(num[0]), int(num[1]) + 1))
            ln.append(range(int(num[2]), int(num[3]) + 1))
            ln.append(range(int(num[4]), int(num[5]) + 1))
            lines.append(ln)
            # lines.append(line)
    return lines

file = read_file('input_day22.txt')
# file2 = read_file2('input_day22.txt')
# d = collections.defaultdict(int)
#
# for i in file2[0:20]:
#     all_cubes = set(itertools.product(set(i[1]), set(i[2]), set(i[3])))
#     value = 1 if i[0] == 'on' else 0
#     for j in all_cubes:
#         d[j] = value
# print(sum(d.values()))

#Idea: https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle
def intersection(x1_min,x2_min, x1_max, x2_max):
    a = (x1_min <= x2_min and x2_min <= x1_max)
    b = (x2_min <= x1_min and x1_min <= x2_max)
    if a or b:
        if a:
            return [x2_min, min(x1_max, x2_max)]
        else:
            return [x1_min, min(x1_max, x2_max)]

cubes_on = []
cubes_off = []
l = 0
for i in file:
    print(l)
    cubes_on_tmp = cubes_on.copy()
    cubes_off_tmp = cubes_off.copy()
    add_to_on = []
    val = True if i[0]=='on' else False
    if val:
        cubes_on_tmp.append((val, i[1], i[2], i[3]))
        for ind, c in enumerate(cubes_on):
            cx = intersection(i[1][0], c[1][0], i[1][1], c[1][1])
            cy = intersection(i[2][0], c[2][0], i[2][1], c[2][1])
            cz = intersection(i[3][0], c[3][0], i[3][1], c[3][1])
            value_off = not c[0]
            try:
                new_off = (value_off, (cx[0], cx[1]), (cy[0], cy[1]),(cz[0], cz[1]))
                cubes_off_tmp.append(new_off)
                cubes_on_tmp.append(new_off)
            except:
                pass
    else:
        for ind, c in enumerate(cubes_on):
            cx = intersection(i[1][0], c[1][0], i[1][1], c[1][1])
            cy = intersection(i[2][0], c[2][0], i[2][1], c[2][1])
            cz = intersection(i[3][0], c[3][0], i[3][1], c[3][1])
            value_off = not c[0]
            try:
                new_off = (value_off, (cx[0], cx[1]), (cy[0], cy[1]), (cz[0], cz[1]))
                cubes_off_tmp.append(new_off)
                cubes_on_tmp.append(new_off)
            except:
                pass
    cubes_off = cubes_off_tmp.copy()
    cubes_on = cubes_on_tmp.copy()
    #print('dydis', len(cubes_on))
    if l == 3:
        print(cubes_on)
    l += 1

cnt = 0
for i in cubes_on:
    if i[0]==True:
        cnt += (abs(i[1][1]-i[1][0])+1) * (abs(i[2][1]-i[2][0])+1) * (abs(i[3][1]-i[3][0])+1)
    else:
        cnt -= (abs(i[1][1]-i[1][0])+1) * (abs(i[2][1]-i[2][0])+1) * (abs(i[3][1]-i[3][0])+1)

print(cnt)