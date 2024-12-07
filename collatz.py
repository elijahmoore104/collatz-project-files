"""
author: Elijah Moore
"""

import matplotlib.pyplot as plt 
import numpy as np
from collatz_functions import *


arr = []
for t in range(1,20):
    seq = getHailstoneSequence(8*t-1)
    arr.append(getCollatzDepth(seq))

print(arr)

# x_val = []
# y_val = []
# arr = []
# max_num = 30

# plot_num = 13

# fig, ax = plt.subplots()

# for t in range(2,100):
#     x = getHailstoneSequence(t)
#     y = range(1,len(x)+1)    
    
#     ax.set_title("Collatz Path: " + str(t))
    
#     ax.set_xlim(0, len(list(y))*1.2)
#     ax.set_ylim(0, max(x)*1.2)

#     ax.set_data(y,x)
    
#     ax.pause(0.1)

# ax.show()

