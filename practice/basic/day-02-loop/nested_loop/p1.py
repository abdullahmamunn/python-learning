# if n = 3 and m = 5 then
# *****
# *****
# *****

def print_nm(n,m):
  for i in range(1, n+1):
    for j in range(1, m+1):
      print("*",end="")

    print()

#print_nm(5,3)


# problem: 02

# *
# **
# ***
# ****
# *****
 
def print_right_pyramid(n):
  for i in range(1, n+1):
    for j in range(1, i+1):
      print("*",end="")

    print()


# print_right_pyramid(5)


# problem: 02

# 1
# 12
# 123
# 1234
# 12345
 
def print_right_pyramid(n):
  for i in range(1, n+1):
    for j in range(1, i+1):
      print("*",end="")

    print()


# print_right_pyramid(5)


# problem: 02

#     1
#    12
#   123
#  1234
# 12345
 
def print_left_pyramid(n):
  for i in range(1, n+1):
    for j in range(n-i):
      print("1",end="")

    print()


print_left_pyramid(5)
