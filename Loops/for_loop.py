# Count 1 to num
num = int(input())

for i in range(1,num, 1): #start, stop, step
    print(i)

# Count from num to zero
num = int(input())

for i in range(num, -1, -1):
    print(i)

# Count step 2 from input num
num = int(input())

for i in range(2,num, 2):
    print(i)

num = int(input())

for i in num:
    print(i)
# output: ValueError: invalid literal

# we can use list, string

name = input()

for i in name:
    print(i)
# output: Abdulah
# A
# b
# d
# u
# l
# a
# h


fruits = ['Apple', 'banana', 'lemon', 'orange']
for f in fruits:
   print(f)

# Apple
# banana
# lemon
# orange

