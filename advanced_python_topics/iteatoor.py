# Python program to demonstrate
# infinite iterators

import itertools

# for in loop
for i in itertools.count(1,1):
    if i ==10:
        break
    else:
        print(i,end=' ')