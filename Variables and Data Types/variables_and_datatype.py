price = 10 #integer
rating = 4.9 #float
name = "Abdullah" #string
is_published = False # boolean

print("Price is ", price)
print("rating is ", rating)
print("name is ", name)
print("is_published = ", is_published)


name = "Abdullah"
course = "Learning Python"
skill = "Python"

# print mew line strategy
print(name, course, skill, sep='\n')
print(f"{name}\n{course}\n{skill}")

# output
"""
Price is  10
rating is  4.9
name is  Abdullah
is_published =  False
"""


# more datatypes
# list, tuple, set, dict

# List store different types of data but you can mutable
my_list = [Abdullah, 26, 506.3, true]

# A tuple is similar to a list, but it cannot be modified (immutable).
my_tupple = ("abdullah", 26, "Dhaka")

# A set is an unordered collection that does not allow duplicate values.
my_sets = {"Abdullah", "Dhaka", "Bangladesh", "26"}  

# A dictionary in Python is a collection of key-value pairs. It is unordered, mutable
my_dict = {
    "name" : "Abdullah",
    "Age"  : 26,
    "Location" : "Dhaka, Bangladesh"
}

print(my_dict)
