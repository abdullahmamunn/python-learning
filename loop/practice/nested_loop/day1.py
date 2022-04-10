# Programs to print number pattern

row = 5
for outer_loop in range(1,row+1):
    for inner_loop in range(outer_loop):
        print(outer_loop,end=' ')
    print("")

num = [4,2,4,1]
for x in num:
    print("*"*x)


























# rows = 5
# for outer_loop in range(1, rows+1):
#     for inner_loop in range(outer_loop):
#         print(outer_loop,end=' ')
#     print("")

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# rows = 5
# for outer_loop in range(rows+1):
#     for inner_loop in range(1, outer_loop+1):
#         print(inner_loop,end=" ")
#     print("")

# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5
# print("\n")
# rows = 5
# num = 0
# for outer_loop in range(rows, 0, -1):
#     num = num + 1
#     for inner_loop in range(outer_loop):
#         print(num, end=' ')
#     print("")
# print("\n")
# 5 5 5 5 5
# 5 5 5 5
# 5 5 5
# 5 5
# 5

# rows = 5
# for outer_loop in range(rows, 0, -1):
#     for inner_loop in range(outer_loop):
#         print(rows, end=' ')
#     print("")