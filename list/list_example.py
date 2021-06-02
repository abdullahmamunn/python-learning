# using list constructor
my_list = list((1, 2, 3))
print(my_list)

#using square brackets[]
my_list1 = [1, 2, 3, 4]
print(my_list1)

#with heterogeneous item
mylist3 = [25, 'mamun', 52.2, True]
print(mylist3)

#empty list using list
mylist4 = list()
print(mylist4)

#empty list using square brackets
mylist5 = []
print(mylist5)

#find length of list
length = len(my_list1)
print(length)

#indexing

list_items = [
    "mamun",
    24.5,
    2021,
    "BUBT",
    "Bajitpur",
    "Kishoreganj"
]
list_items[0] = "Abdullah"
print(len(list_items))
print(list_items)

# slicing all items
print(list_items[0:])

# slicing first four items
print(list_items[:4])

#print every second element with a skip count 2
print(list_items[::2])

#reversing the list
print(list_items[::-1])

#start of 3rd item to last item
print(list_items[3:])

#iterating a list

for items in list_items:
    print(items)
#iterate along with index number
for i in range(0, len(list_items)):
    print("[{0}]".format(i), list_items[i])

#Adding elements to the list
# with Append, insert and extends
#append() method will accept only one parameter and add to the end of the list
list_items.append('Humaypur')
for i in range(0, len(list_items)):
    print("[{0}]".format(i), list_items[i])

# insert() method will accept two parameters position and object. You can insert any position using insert method in list.
list_items.insert(7, "Durighagatia")
for i in range(0, len(list_items)):
    print("[{0}]".format(i), list_items[i])