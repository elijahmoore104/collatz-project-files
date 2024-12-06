"""

author: Elijah Moore

"""

from collatz_functions import *
import numpy as np 
import matplotlib.pyplot as plt


outputArr = []


for i in range(0, 101):
        outputArr.append(getCollatzDepth(getCollatzPath(i)))
        outputArr.append(len(getCollatzPath(i))) 

print(getIndexPositions(outputArr, 11))
duplic_check = {i : outputArr.count(i) for i in outputArr}


print(getReverseCollatzPath(20))
