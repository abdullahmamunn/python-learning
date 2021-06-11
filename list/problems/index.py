# Remove duplicate items in a list
mylist = [10,2,3,10,5,2,10]
mylist2 = []
for items in mylist:
    if items not in mylist2:
        mylist2.append(items)
print(mylist2)

#Find max value in a list
my_list = [1000.1, 2, 3, 1000.4, 500, 2, 10]
max = my_list[0]
for item in my_list:
    if item > max:
        max = item
print(max)