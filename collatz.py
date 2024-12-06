"""

author: Elijah Moore

"""

import matplotlib.pyplot as plt 
import numpy as np

from collatz_functions import *

x_val = []
y_val = []
arr = []

max_num = 30
plot_num = 13


for t in range(2,100):
    x = getCollatzPath(t)
    y = range(1,len(x)+1)    
    
    ax.set_title("Collatz Path: " + str(t))
    
    ax.set_xlim(0, len(list(y))*1.2)
    ax.set_ylim(0, max(x)*1.2)

    data.set_data(y,x)
    
    plt.pause(0.1)

plt.show()

