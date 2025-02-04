# reverse array

list = [10, 20, 30, 40]
list2 = []

# using loop
for i in range(len(list)-1, -1, -1):
  list2.append(list[i])
print("Reversed with loop: "," ".join(map(str, list2)))

# use array index
reversed_array = list[::-1] #slicing
# sequence[start:stop:step]
print("Reverse with slicing: "," ".join(map(str, reversed_array)))

reversed_ = reversed(list)
print("Reverse with reversed: "," ".join(map(str, reversed_)))


list.reverse()

print("Reverse with reverse function: "," ".join(map(str, (list))))
