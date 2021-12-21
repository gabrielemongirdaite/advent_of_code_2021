import numpy as np
import itertools
import functools
import time
import collections

#@functools.lru_cache(maxsize=None)
def step_calc(i, k):
    return 10.0 if (i + k) % 10.0 == 0.0 else (i + k) % 10.0


universes = {(6.0,0.0, 2.0, 0.0):1.0}#{'4-8': [(1, 0, 0)]}
split_universe = [3.0]+[4.0]*3+[5.0]*6+[6.0]*7+[7.0]*6+[8.0]*3+[9.0] #[(3,1), (4,3), (5,6), (6,7), (7,6), (8,3), (9,1)]#
print(split_universe)

def one_split_first(universe):
    global split_universe
    wins = 0
    new_universes = []
    for i in split_universe:
        step = step_calc(universe[0], i)
        score = universe[1]+step
        if score>=21:
            wins += 1.0
        else:
            new_universes.append((step,score, universe[2], universe[3]))
    return wins, collections.Counter(new_universes)



def one_split_second(universe):
    global split_universe
    wins = 0
    new_universes = []
    for i in split_universe:
        step = step_calc(universe[2], i)
        score = universe[3]+step
        if score>=21:
            wins += 1.0
        else:
            new_universes.append((universe[0], universe[1],step,score))
    return wins, collections.Counter(new_universes)


n = 0
wins_1 = 0.0
wins_2 = 0.0
while universes!= {}:
    print(n)
    universes_temp = {}
    for i, value in universes.items():
        if n % 2 ==0:
            wins, new_universes = one_split_first(i)
            wins_1 += wins*value
        else:
            wins, new_universes = one_split_second(i)
            wins_2+=wins*value
        universes_temp = {k: universes_temp.get(k, 0) + new_universes.get(k, 0)*value for k in set(universes_temp) | set(new_universes)}
    universes = universes_temp.copy()
    print(wins_1, wins_2)
    n += 1