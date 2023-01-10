# -*- coding: utf-8 -*-

import itertools
import numpy as np
from random import sample

reds = []
for i in itertools.combinations(np.arange(1, 34), 6):
    reds.append(sorted(list(i)))
# print(reds)

blue = []
for i in itertools.combinations(np.arange(1, 17), 1):
    blue.append(list(i))
# print(blue)

cn = 1 * 2 * 2 * 2 * 3 * 3 * 8
print("共买了" + str(cn) + "注")
rs = sample(list(itertools.product(reds, blue)), cn)


# print(rs)


def win(r, t):
    if r == t:
        print(str(r) + "中了" + str(t) + "一等奖 耶耶耶耶耶耶")
        return
    if r[:6] == t[:6]:
        print(str(r) + "中了" + str(t) + "二等奖 耶耶耶")
        return
    for i in itertools.combinations(r[:6], 5):
        if set(i) < set(t[:6]) and r[6] == t[6]:
            print(str(r) + "中了" + str(t) + "三等奖 耶")
            return
    if r[6] == t[6]:
        for i in itertools.combinations(r[:6], 4):
            if set(i) < set(t[:6]):
                print(str(r) + "中了" + str(t) + "四等奖")
                return
        for i in itertools.combinations(r[:6], 3):
            if set(i) < set(t[:6]):
                print(str(r) + "中了" + str(t) + "五等奖")
                return
    else:
        for i in itertools.combinations(r[:6], 5):
            if set(i) < set(t[:6]):
                print(str(r) + "中了" + str(t) + "四等奖")
                return
        for i in itertools.combinations(r[:6], 4):
            if set(i) < set(t[:6]):
                print(str(r) + "中了" + str(t) + "五等奖")
                return

    if r[6] == t[6]:
        print(str(r) + "中了" + str(t) + "六等奖")
        return


t1 = [1, 7, 15, 16, 20, 25, 16]
t2 = [5, 8, 18, 25, 30, 32, 6]
t3 = [2, 6, 10, 16, 18, 22, 13]
t4 = [9, 16, 18, 22, 28, 32, 2]
# t5 = [1, 7, 11, 12, 22, 28, 5]
# t6 = [2, 22, 26, 29, 32, 33, 14]
for t_i in [t1, t2, t3, t4]:
    for r_i in rs:
        win(r_i[0] + r_i[1], t_i)
