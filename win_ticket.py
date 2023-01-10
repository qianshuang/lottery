# -*- coding: utf-8 -*-

import itertools
import numpy as np
import pandas as pd

red0 = [1]
red1 = [6, 7]
red2 = np.arange(13, 16)
red3 = np.arange(20, 23)
red4 = [26, 27]
red5 = [32, 33]
blue = [1, 16, 12, 9, 15, 7, 14, 11]
print("共购买" + str(len(list(itertools.product(red0, red1, red2, red3, red4, red5, blue)))) + "注")


# blue = np.arange(1, 17)


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
t5 = [1, 7, 11, 12, 22, 28, 5]
t6 = [2, 22, 26, 29, 32, 33, 14]
for t_i in [t1, t2, t3, t4]:
    for r_i in itertools.product(red0, red1, red2, red3, red4, red5, blue):
        win(list(r_i), t_i)

# df = pd.read_csv("data/balls_data.txt", sep=" ", header=None)
# for row in df.iterrows():
#     t_i = [row[1][1], row[1][2], row[1][3], row[1][4], row[1][5], row[1][6], row[1][7]]
#     print(t_i)
#     for r_i in itertools.product(red0, red1, red2, red3, red4, red5, blue):
#         win(list(r_i), t_i)
