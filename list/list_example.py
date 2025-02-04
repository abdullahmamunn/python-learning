# using list constructor
my_list = list((1, 2, 3))
print(my_list)

# output: [1, 2, 3]

# using square brackets[]
my_list1 = [1, 2, 3, 4]
print(my_list1)

# output: [1, 2, 3, 4]

# with heterogeneous items
mylist3 = [25, 'mamun', 52.2, True]
print(mylist3)

# Output: [25, 'mamun', 52.2, True]

# empty list using list
mylist4 = list()
print(mylist4)

# Output: []

# empty list using square brackets
mylist5 = []
print(mylist5)

# Output: []

# find length of list
ls = [1,2.2,"mamun",False, True, 124]
length = len(ls)
print(f"Length is {length}")

# indexing

list_items = [
    "mamun",
    24.5,
    2021,
    "BUBT",
    "Bajitpur",
    "Kishoreganj"
]
list_items[0] = "Abdullah" # modify items
print(len(list_items)) #Output: 6
print(list_items) #Output: ['Abdullah', 24.5, 2021, 'BUBT', 'Bajitpur', 'Kishoreganj']

# slicing all items
print(list_items[0:])

# slicing first four items
print(list_items[:4])

# print every second element with a skip count 2
print(list_items[::2])

# reversing the list
print(list_items[::-1])

# start of 3rd item to last item
print(list_items[3:])

# iterating a list
for items in list_items:
    print(items)
# iterate along with index number
for i in range(0, len(list_items)):
    print("[{0}]".format(i), list_items[i])

# Adding elements to the list
# with Append, insert and extends
# append() method will accept only one parameter and add to the end of the list
list_items.append('Humaypur')
for i in range(0, len(list_items)):
    print("[{0}]".format(i), list_items[i])

# insert() method will accept two parameters position and object. You can insert any position using insert method in list.
list_items.insert(0, "Durighagatia")
for i in range(0, len(list_items)):
    print("")
    print("[{0}]".format(i), list_items[i])

# Modify all items
mylists = [9, 2, 7, 4, 5]
for i in range(len(mylists)):
    sq = mylists[i]*mylists[i]
    mylists[i] = sq
print(mylists)

# Find the max value in a list
max = mylists[0]
for number in mylists:
    if number > max:
        max = number
print(max)

# Removing elements from a List

mylists.remove(25)
mylists.pop(0)
del mylists[1:2]
mylists.clear()
print(mylists)

# Finding an element of index in the list, using index() function
finding = [10, 20, 20, 30, 40, 50, 80]
print(finding.index(80))
# Concat two string
finding2 = [800, 700, 600]
concat = finding + finding2
finding.extend(finding2) # First list er vitore 2nd list extends kore dichi
print(finding)
print(concat)

# Using the copy() method
# List operations
# We can perform some operations over the list by using certain functions like sort(), reverse(), clear() etc.
sorting = [1,5,3,4,10,9,100,99]
sorting.sort()
print(sorting)

# Reverse a List using reverse()
sorting.reverse()
print(sorting)

# print max and min value
maxmin2 = [1, 5, 3, 4]
print(sum(maxmin2))
print(min(maxmin2))

#with all true values
samplelist1 = [1, 1, True]
print("all() All True values::", all(samplelist1))

#with one false
samplelist2 = [0, 1, True, 1]
print("all() with One false value ::", all(samplelist2))

# any()
# The any() method will return true if there is at least one true value.
# In the case of Empty List, it will return false.
