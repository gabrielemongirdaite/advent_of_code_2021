import itertools
from collections import Counter
from functools import reduce
import copy

def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            line = line.replace('\n', '')
            lines.append(line)
        indices = [i+1 for i, x in enumerate(lines) if x == ""]
        indices.insert(0, 0)
        indices.append(len(lines))
        result = [lines[x:y] for x,y in zip(indices, indices[1:])]
        result = [i[1:] for i in result]
        for L in result:
            try:
                L.remove('')
            except ValueError:
                pass
        result2 = []
        for i in result:
            tmp = []
            for j in i:
                tmp.append([int(k) for k in j.split(',')])
            result2.append(tmp)
    return result2

def rec_abs(a):
    for i, el in enumerate(a):
        a[i] = rec_abs(el) if isinstance(el, list) else abs(a[i])

    return a

def check_if_order_fine(subtraction_xyz, sum_xyz):
    x_sum_freq = Counter([k[0] for k in sum_xyz.values()]).most_common(1)[0][1]
    x_sum_value = Counter([k[0] for k in sum_xyz.values()]).most_common(1)[0][0]
    x_sub_freq = Counter([k[0] for k in subtraction_xyz.values()]).most_common(1)[0][1]
    x_sub_value = Counter([k[0] for k in subtraction_xyz.values()]).most_common(1)[0][0]

    y_sum_freq = Counter([k[1] for k in sum_xyz.values()]).most_common(1)[0][1]
    y_sum_value = Counter([k[1] for k in sum_xyz.values()]).most_common(1)[0][0]
    y_sub_freq = Counter([k[1] for k in subtraction_xyz.values()]).most_common(1)[0][1]
    y_sub_value = Counter([k[1] for k in subtraction_xyz.values()]).most_common(1)[0][0]

    z_sum_freq = Counter([k[2] for k in sum_xyz.values()]).most_common(1)[0][1]
    z_sum_value = Counter([k[2] for k in sum_xyz.values()]).most_common(1)[0][0]
    z_sub_freq = Counter([k[2] for k in subtraction_xyz.values()]).most_common(1)[0][1]
    z_sub_value = Counter([k[2] for k in subtraction_xyz.values()]).most_common(1)[0][0]

    return max(x_sub_freq, x_sum_freq)>=12 and max(y_sub_freq, y_sum_freq)>=12 and max(z_sub_freq, z_sum_freq)>=12,\
    x_sub_value if x_sub_freq>=x_sum_freq else x_sum_value,\
    y_sub_value if y_sub_freq>=y_sum_freq else y_sum_value,\
    z_sub_value if z_sub_freq>=z_sum_freq else z_sum_value,\
    -1 if x_sub_freq>=x_sum_freq else 1,\
    -1 if y_sub_freq>=y_sum_freq else 1,\
    -1 if z_sub_freq>=z_sum_freq else 1

def direction_order_abs(subtraction_xyz, sum_xyz, order):
    check = check_if_order_fine(subtraction_xyz, sum_xyz)
    x_abs = check[1]
    y_abs = check[2]
    z_abs = check[3]
    direction = (check[4], check[5], check[6])
    order = order
    return x_abs, y_abs, z_abs, direction, order, subtraction_xyz, sum_xyz

def find_indices(sum_list, subtraction_list, direction, n, xyz_abs):
    if direction[n]==-1:
        indices = [k for  k in subtraction_list if subtraction_list[k][n]==xyz_abs]
    else:
        indices = [k for  k in sum_list if sum_list[k][n] == xyz_abs]
    return indices

def comparison(scanners, comb):
    global dict_path
    global full_list
    global scann
    first = copy.deepcopy(scanners[comb[0]])
    second = copy.deepcopy(scanners[comb[1]])
    first = rec_abs(first)
    second = rec_abs(second)
    subtraction_xyz= {}
    sum_xyz= {}
    subtraction_xzy={}
    sum_xzy={}

    subtraction_yxz={}
    sum_yxz={}
    subtraction_yzx={}
    sum_yzx={}

    subtraction_zxy={}
    sum_zxy={}
    subtraction_zyx={}
    sum_zyx={}
    for ind1, i in enumerate(first):
        for ind2, j in enumerate(second):
            subtraction_xyz[str(ind1)+'-'+str(ind2)] = [abs(x-y) for x,y in zip(i,j)]
            sum_xyz[str(ind1)+'-'+str(ind2)] = [x + y for x, y in zip(i, j)]
            subtraction_xzy[str(ind1)+'-'+str(ind2)] = [abs(x-y) for x, y in zip(i, [j[0], j[2], j[1]])]
            sum_xzy[str(ind1)+'-'+str(ind2)] = [x + y for x, y in zip(i, [j[0], j[2], j[1]])]

            subtraction_yxz[str(ind1)+'-'+str(ind2)] = [abs(x-y) for x, y in zip(i, [j[1], j[0], j[2]])]
            sum_yxz[str(ind1)+'-'+str(ind2)] = [x + y for x, y in zip(i, [j[1], j[0], j[2]])]
            subtraction_yzx[str(ind1)+'-'+str(ind2)] = [abs(x-y) for x, y in zip(i, [j[1], j[2], j[0]])]
            sum_yzx[str(ind1)+'-'+str(ind2)] = [x + y for x, y in zip(i, [j[1], j[2], j[0]])]

            subtraction_zxy[str(ind1)+'-'+str(ind2)] = [abs(x-y) for x, y in zip(i, [j[2], j[0], j[1]])]
            sum_zxy[str(ind1)+'-'+str(ind2)] = [x + y for x, y in zip(i, [j[2], j[0], j[1]])]
            subtraction_zyx[str(ind1)+'-'+str(ind2)] = [abs(x-y) for x, y in zip(i, [j[2], j[1], j[0]])]
            sum_zyx[str(ind1)+'-'+str(ind2)] = [x + y for x, y in zip(i, [j[2], j[1], j[0]])]


    if check_if_order_fine(subtraction_xyz, sum_xyz)[0]:
        x_abs, y_abs, z_abs, direction, order, subtraction_list, sum_list = direction_order_abs(subtraction_xyz, sum_xyz, [0,1,2])
    elif check_if_order_fine(subtraction_xzy, sum_xzy)[0]:
        x_abs, y_abs, z_abs, direction, order, subtraction_list, sum_list = direction_order_abs(subtraction_xzy, sum_xzy, [0,2,1])
    elif check_if_order_fine(subtraction_yxz, sum_yxz)[0]:
        x_abs, y_abs, z_abs, direction, order, subtraction_list, sum_list = direction_order_abs(subtraction_yxz, sum_yxz, [1,0,2])
    elif check_if_order_fine(subtraction_yzx, sum_yzx)[0]:
        x_abs, y_abs, z_abs, direction, order, subtraction_list, sum_list = direction_order_abs(subtraction_yzx, sum_yzx, [1,2,0])
    elif check_if_order_fine(subtraction_zxy, sum_zxy)[0]:
        x_abs, y_abs, z_abs, direction, order, subtraction_list, sum_list = direction_order_abs(subtraction_zxy, sum_zxy, [2,0,1])
    elif check_if_order_fine(subtraction_zyx, sum_zyx)[0]:
        x_abs, y_abs, z_abs, direction, order, subtraction_list, sum_list = direction_order_abs(subtraction_zyx, sum_zyx, [2,1,0])
    try:
        #print(x_abs, y_abs, z_abs)
        x_indices = find_indices(sum_list, subtraction_list,direction, 0, x_abs)
        y_indices = find_indices(sum_list, subtraction_list,direction, 1, y_abs)
        z_indices = find_indices(sum_list, subtraction_list,direction, 2, z_abs)
        d = [x_indices, y_indices, z_indices]
        inter = list(reduce(set.intersection, [set(item) for item in d]))
        lst_ind = []
        for k in inter:
            spl = k.split('-')
            f = int(spl[0])
            s = int(spl[1])
            lst_ind.append((f,s))
            #print(scanners[comb[0]][f], scanners[comb[1]][s])
        x_final = scanners[comb[1]][lst_ind[0][1]][order[0]]+scanners[comb[0]][lst_ind[0][0]][0] \
            if abs(scanners[comb[1]][lst_ind[0][1]][order[0]]+scanners[comb[0]][lst_ind[0][0]][0])==x_abs \
            else scanners[comb[0]][lst_ind[0][0]][0] - scanners[comb[1]][lst_ind[0][1]][order[0]]
        y_final = scanners[comb[1]][lst_ind[0][1]][order[1]] + scanners[comb[0]][lst_ind[0][0]][1]\
            if abs(scanners[comb[1]][lst_ind[0][1]][order[1]] + scanners[comb[0]][lst_ind[0][0]][1])==y_abs \
            else scanners[comb[0]][lst_ind[0][0]][1] - scanners[comb[1]][lst_ind[0][1]][order[1]]
        z_final = scanners[comb[1]][lst_ind[0][1]][order[2]] + scanners[comb[0]][lst_ind[0][0]][2]  \
            if abs(scanners[comb[1]][lst_ind[0][1]][order[2]] + scanners[comb[0]][lst_ind[0][0]][2])==z_abs \
            else scanners[comb[0]][lst_ind[0][0]][2] - scanners[comb[1]][lst_ind[0][1]][order[2]]
        direction = (-1 \
            if abs(scanners[comb[1]][lst_ind[0][1]][order[0]]+scanners[comb[0]][lst_ind[0][0]][0])==x_abs \
            else 1, \
                     -1 \
                         if abs(
                         scanners[comb[1]][lst_ind[0][1]][order[1]] + scanners[comb[0]][lst_ind[0][0]][1]) == y_abs \
                         else 1, \
                     -1 \
                         if abs(
                         scanners[comb[1]][lst_ind[0][1]][order[2]] + scanners[comb[0]][lst_ind[0][0]][2]) == z_abs \
                         else 1
                     )
        #print('scanner', str(comb[1]), 'must be at (', x_final, y_final, z_final, ') relative to scanner', str(comb[0]), direction, order)
        #
        # redo the input file. Aim to get all ordered at [0,1,2] with direction = (1,1,1)
        # print('--- scanner '+str(comb[1])+' ---')
        # for k in scanners[comb[1]]:
        #     print(k[order[0]]*direction[0],',', k[order[1]]*direction[1],',', k[order[2]]*direction[2])
        # print('')
        # print('comparison(scanners, ('+str(comb[0])+','+str(comb[1])+'))')

        dict_path[' '+str(comb[1])+'-'+str(comb[0])] = [(x_final, y_final, z_final), direction, order]
        k = ' '
        xyz = dict_path[' '+str(comb[1]) + '-' + str(comb[0])][0]
        direction = dict_path[' '+str(comb[1]) + '-' + str(comb[0])][1]
        order = dict_path[' '+str(comb[1]) + '-' + str(comb[0])][2]
        initial = comb[0]
        all_beacons = scanners[comb[1]]
        if comb[0]==0:
            for i in all_beacons:
                k = [i[order[0]] * direction[0] + xyz[0],
                      i[order[1]] * direction[1] + xyz[1], i[order[2]] * direction[2] + xyz[2]]
                if k not in full_list:
                    full_list.append(k)
            scann.append(xyz)
        if comb[0]!=0:
            direction_old = direction
            order_old = order
            all_k = []
            while '-0' not in k and k!='' : #k not in all_k #added when finding the pairs
                direction =1
                k = [key for key in dict_path if ' '+str(initial)+'-' in key][0]
                #print(k)
                all_k.append(k)
                xyz1 = dict_path[k][0]
                direction1 = dict_path[k][1]
                order1 = dict_path[k][2]
                x = xyz1[0] - xyz[order1[0]] if direction1[0]==-1 else xyz1[0] + xyz[order1[0]] #xyz1[0] - xyz[order1[0]]*(-1 if direction[order1[0]]!=direction1[0] else 1)
                y = xyz1[1] - xyz[order1[1]] if direction1[1]==-1 else xyz1[1] + xyz[order1[1]] #xyz1[1] - xyz[order1[1]] * (-1 if direction[order1[1]] != direction1[1] else 1)
                z = xyz1[2] - xyz[order1[2]] if direction1[2]==-1 else xyz1[2] + xyz[order1[2]] #xyz1[2] - xyz[order1[2]] * (-1 if direction[order1[2]] != direction1[2] else 1)
                xyz = (x, y, z)
                #print(xyz)
                initial = k.split('-')[1]
                direction *= direction1
                order_old=[order_old[order1[0]],order_old[order1[1]],order_old[order1[2]]]
                order = order1

            if '-0'  in k:
                for i in all_beacons:
                    k = [i[order_old[order[0]]] * direction_old[0]*direction[0] + xyz[0],
                                    i[order_old[order[1]]] * direction_old[1]*direction[1] + xyz[1],
                                    i[order_old[order[2]]] * direction_old[2]*direction[2] + xyz[2]]
                    if k not in full_list:
                        full_list.append(k)
                scann.append(xyz)
    except:
        pass
    return


scanners = read_file('input_day19.txt')
comb = list(itertools.permutations(range(len(scanners)), 2))
dict_path = {}
full_list = []
scann = []
#done in excel
comparison(scanners, (0,1))
comparison(scanners, (0,8))
comparison(scanners, (0,9))
comparison(scanners, (1,11))
comparison(scanners, (1,14))
comparison(scanners, (1,20))
comparison(scanners, (1,21))
comparison(scanners, (9,27))
comparison(scanners, (11,7))
comparison(scanners, (11,10))
comparison(scanners, (11,15))
comparison(scanners, (7,2))
comparison(scanners, (7,4))
comparison(scanners, (7,12))
comparison(scanners, (7,19))
comparison(scanners, (2,13))
comparison(scanners, (2,18))
comparison(scanners, (4,3))
comparison(scanners, (4,17))
comparison(scanners, (10,6))
comparison(scanners, (6,16))
comparison(scanners, (6,25))
comparison(scanners, (13,22))
comparison(scanners, (27,23))
comparison(scanners, (23,24))
comparison(scanners, (22,5))
comparison(scanners, (5,26))

#finding pairs
# for i in comb:
#     comparison(scanners, (i[0], i[1]))
for i in scanners[0]:
    if i not in full_list:
        full_list.append(i)

print(full_list)
print(len(full_list))
max_dist = 0
for i in scann:
    for j in scann:
        dist = abs(i[0]-j[0])+abs(i[1]-j[1])+abs(i[2]-j[2])
        max_dist = dist if dist>max_dist else max_dist

print(max_dist)