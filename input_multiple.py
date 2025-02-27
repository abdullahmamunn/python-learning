# Python program showing how to
# multiple input using split

# taking two inputs at a time
x, y = nput("Enter a two value: ").split()i
print("Number of boys: ", x)
print("Number of girls: ", y)

"""
Enter a two value: 5 5
Number of boys:  5
Number of girls:  5

"""
print()

# taking three inputs at a time
x, y, z = input("Enter a three value: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)

"""
Enter a three value: 1 2 3
Total number of students:  1
Number of boys is :  2
Number of girls is :  3
"""
print()

# taking two inputs at a time
a, b = input("Enter a two value: ").split()
print("First number is {} and second number is {}".format(a, b))
"""
Enter a two value: 2 2
First number is 2 and second number is 2
"""
print()

# taking multiple inputs at a time
# and type casting using list() function
x = list(map(int, input("Enter a multiple value: ").split()))
print("List of students: ", x)

"""
Enter a multiple value: 10 15 20 25 30 100
List of students:  [10, 15, 20, 25, 30, 100]
"""
