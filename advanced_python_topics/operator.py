# Python program to demonstrate
# iterator module

import operator
import time

# Defining lists
L1 = [5, 0, 31]
L2 = [2, 1, 31]

# Starting time before map
# function
t1 = time.time()

# Calculating result
a, b, c = map(operator.add, L1,L2)
t2 = time.time()
print(a,b,c)
print(t2,t1)
print("time taken by map function %.6f"%(t2-t1))