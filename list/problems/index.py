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

# product all list elements
multiplicands = [1, 2, 3, 4, 5]
product = 1
for multi in multiplicands:
    product = product * multi
print(product)

# sum all list items
sum_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 1
for item in sum_items:
    sum = sum + item
print(sum)


squares = [n**2 for n in range(10)]
print(squares)

squares1 = []
for n in range(10):
    squares1.append(n**2)
squares1.pop(8)
print(squares1)