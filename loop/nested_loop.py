#nested for loop example
# for outer_loop in range(3):
#     for inner_loop in range(1, 3):
#         print(outer_loop, inner_loop)

# for outer_loop in range(0, 3):
#     for inner_loop in range(1, 4):
#         print(outer_loop, inner_loop)
# items = [5, 2, 5, 2, 2]
# for item in items:
#     print('*'*item)

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# for outer_loop in range(1,6):
#     for inner_loop in range(1, outer_loop+1):
#         print(inner_loop, end=' ')
#     print("")

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# for outer_loop in range(1,6):
#     for inner_loop in range(1, outer_loop+1):
#         print(outer_loop, end=' ')
#     print("")

# 1 1 1 1 1
# 1 1 1 1
# 1 1 1
# 1 1
# 1

# for outer_loop in range(5, 0, -1):
#     for inner_loop in range(outer_loop):
#         print('1', end=' ')
#     print('')


# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

# count = 0
# for outer_loop in range(5, 0, -1):
#     count += 1
#     for inner_loop in range(outer_loop):
#         print(count, end=' ')
#     print('')

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

rows = int(input())
num = rows
for outer_loop in range(1,rows*2):
    for inner_loop in range(1, outer_loop):
            if inner_loop %2 == 1:
                print(inner_loop, end=' ')
    print("")