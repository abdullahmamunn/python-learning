array1 = [1, 2, 3, 4]
array2 = [1, 2, 3, 4]

array3 = array1 + array2
print(f"Marge { array1 } and { array2} "," ".join(map(str, array3)))

# use extend()

array1.extend(array2)

print(" ".join(map(str,array1)))


# using loop

# for item in array1:
#   array2.append(item)

# print(array2)


