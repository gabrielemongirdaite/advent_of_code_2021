from sympy import solve
from sympy.abc import x
import math
value = []
steps = []
velocity_x = []

for i in range(0,194):
    for j in range(0,i):
        v = sum(range(i,j,-1))
        s = i-j
        vel_x = i
        if v>=150 and v<=193:
            value.append(v)
            steps.append(s)
            velocity_x.append(vel_x)

not_equal_steps = [x for x,y in zip(steps, velocity_x) if x!=y]
not_equal_velocity_x = [y for x,y in zip(steps, velocity_x) if x!=y]
equal_steps = [x for x,y in zip(steps, velocity_x) if x==y]
equal_velocity_x = [y for x,y in zip(steps, velocity_x) if x==y]

all = []
for ind, i in enumerate(not_equal_steps):
    t = sum(range(0, i))
    for j in list(range(math.ceil(solve(i*x-t+136, x)[0]), math.floor(solve(i*x-t+86, x)[0]) + 1)):
        if (not_equal_velocity_x[ind], j) not in all:
            all.append((not_equal_velocity_x[ind], j))


max_step = 135
max_length = range(0,max_step+1)

def if_in_target(y, step_min):
    y_temp = y
    y_sum = y
    step = 1
    not_in_target = True
    while not_in_target or y_sum>=-136:
        y_temp -=1
        y_sum += y_temp
        step += 1
        if y_sum<=-86 and y_sum>=-136 and step>=step_min:
            not_in_target = False
    return not_in_target

def if_in_target(y, step_min):
    y_temp = y
    y_sum = y
    step = 1
    not_in_target = True
    while not_in_target and y_sum>=-136:
        y_temp -=1
        y_sum += y_temp
        step += 1
        if y_sum<=-86 and y_sum>=-136 and step>=step_min:
            not_in_target = False
    return not_in_target

for ind, i in enumerate(equal_velocity_x):
    for j in max_length:
        if (i, j) not in all and not if_in_target(j, equal_steps[ind]):
            all.append((i, j))

print(sum(max_length))
print(len(all))