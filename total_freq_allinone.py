# -*- coding: utf-8 -*-

import pandas as pd
from collections import Counter

from matplotlib import pyplot as plt

all_data = []
df = pd.read_csv("data/balls_data.txt", sep=" ", header=None)
for i in range(1, 7):
    all_data.extend(list(df.iloc[:, i].values))
print(all_data)
val_cnt = dict(Counter(all_data))
print(val_cnt)
print(sorted(val_cnt.items(), key=lambda x: x[1], reverse=True))
val_cnt = sorted(val_cnt.items(), key=lambda x: x[0])
print(val_cnt)

# plt.plot(range(1, 34), val_cnt, "bo:")
# plt.xlabel('ball number')
# plt.ylabel('cnt')
# plt.show()
