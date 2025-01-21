# Write a program to copy an array into another array and print both array. (the size of the array should be taken from keyboard)


size = int(input("Enter array size: "))

array_A = list(map(int, (input(f"Enter {size} numbers: ").split())))

if size != len(array_A):
  print("pelase enter correct size of numbers")
else:
  array_B = array_A
  # Print both arrays
  print("Array A:", "".join(map(str, array_A)))
  print("Array B:", " ".join(map(str, array_B)))


print("Array :", "-".join(map(str, "1315")))


