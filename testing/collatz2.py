"""

author: Elijah Moore

"""

import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.animation as animation


#x_val = []
#y_val = []
#arr = []

max_num = 30
plot_num = 13

#for i in range(0,max_num):
#    arr.append(getCollatzPath(i))

#plt.plot(arr[plot_num], "-o")
#plt.title("Collatz Path: " + str(plot_num))

#plt.pause(5)

fig, ax = plt.subplots()

#path2, = ax.plot(getCollatzPath(2))
#path3, = ax.plot(getCollatzPath(3))

#print( getCollatzPath(3).index(max(getCollatzPath(3))) )

#print(getCollatzPath(3)[3])


for t in range(2,21):
    plot_iteration = 2**t

    y = getCollatzPath(plot_iteration)
    x = range(1,len(y)+1)    
    
    ax.set_title("Collatz Path: " + str(plot_iteration))
    ax.plot(y, "-o")
    
    plt.pause(0.5)

plt.show()




for i in range(0,max_num):
   arr.append(getCollatzPath(i))

plt.plot(arr[plot_num], "-o")
plt.title("Collatz Path: " + str(plot_num))

plt.pause(5)
# 

fig, ax = plt.subplots()