# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
# from matplotlib import pyplot as plt

df = pd.read_csv("data/balls_data.txt", sep=" ", header=None)
df = df[df[2] == 5]
print(df)

col = df.iloc[:, 3]

ball = np.arange(1, 34)
value_cnts = []

for b in ball:
    if b not in col.value_counts():
        value_cnts.append(0)
    else:
        value_cnts.append(col.value_counts()[b])
print(sorted(zip(ball, value_cnts), key=lambda x: x[1], reverse=True))

# plt.plot(ball, value_cnts, "bo:")
# plt.xlabel('ball number')
# plt.ylabel('cnt')
# plt.show()
