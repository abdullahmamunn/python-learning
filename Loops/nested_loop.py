#nested for loop example
for outer_loop in range(3):
  for inner_loop in range(1,3):
    print(f"{(outer_loop,inner_loop)}", end=" ")
  
  print()

#   Output:

# (0, 1) (0, 2) 
# (1, 1) (1, 2) 
# (2, 1) (2, 2) 



for outer_loop in range(0, 3):
    for inner_loop in range(1, 4):
        print(outer_loop, inner_loop)

# output will be:
# 0 1
# 0 2
# 0 3
# 1 1
# 1 2 
# 1 3

items = [5, 2, 5, 2, 2]
for item in items:
    print('*'*item)

# output:
# *****
# **
# *****
# **
# **


for outer_loop in range(1,6):
    for inner_loop in range(1, outer_loop+1):
        print(inner_loop, end=' ')
    print("")

# output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


for outer_loop in range(1,6):
    for inner_loop in range(1, outer_loop+1):
        print(outer_loop, end=' ')
    print("")

# output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5


for outer_loop in range(5, 0, -1):
    for inner_loop in range(outer_loop):
        print('1', end=' ')
    print('')

# output:
# 1 1 1 1 1 
# 1 1 1 1 
# 1 1 1 
# 1 1 
# 1


count = 0
for outer_loop in range(5, 0, -1):
    count += 1
    for inner_loop in range(outer_loop):
        print(count, end=' ')
    print('')


#next day

# 5 5 5 5 5
# 5 5 5 5
# 5 5 5
# 5 5
# 5

# rows = int(input())
# num = rows
# for outer_loop in range(rows, 0, -1):
#     for inner_loop in range(outer_loop):
#         print(num, end=' ')
#     print("")

# 0 1 2 3 4 5
# 0 1 2 3 4
# 0 1 2 3
# 0 1 2
# 0 1

# rows = int(input())
# num = rows
# for outer_loop in range(rows, 1, -1):
#     for inner_loop in range(outer_loop):
#         print(inner_loop,end=' ')
#     print("")

# 1
# 3 3
# 5 5 5
# 7 7 7 7
# 9 9 9 9 9

# rows = int(input())
# num = rows
# for outer_loop in range(1,rows*2):
#     for inner_loop in range(1, outer_loop):
#             if inner_loop %2 == 1:
#                 print(inner_loop, end=' ')
#     print("")

# Print reverse number from 10 to 1
# 1
# 3 2
# 6 5 4
# 10 9 8 7

rows = 5
for outer_loop in range(1, rows):
    for inner_loop in range(1, outer_loop):
        print(inner_loop, end=' ')
    print(" ")