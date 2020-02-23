import random
from itertools import groupby

num_of_streaks = 0
my_list = []
coin_side = 0

for exp_num in range(100):

    for i in range(100):
        coin_side = random.randint(0,1)
        if coin_side == 0:
            my_list += ['H']
        else:
            my_list += ['T']

    groups = groupby(my_list)
    result = [(label, sum(1 for _ in group)) for label, group in groups]

    for l in result:
        if l[1] == 6:
            num_of_streaks += 1

print('Chance of streak:  ' + str(num_of_streaks/100))