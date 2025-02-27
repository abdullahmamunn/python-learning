# Write a program in C to find the maximum and minimum elements in an array.

list = [1,12,3,4,5]

max = 0;

for num in list:
  if num > max:
    max = num

print(f"max is {max}")


# Given an array. Insert a new value in a specific index and reorder the array again.
# Given an array. Remove a specific index element and reorder the array again.


list = [1,2,4,5,6,7,8,9]
list.insert(2,3)
print(list)
list.pop(3)
print(list)


# Write a program that calculates the summation of all rich numbers of an array. A rich number is a number that is greater than all the previous elements.
# Write a program in C to find the second largest element in an array.


# Write a program to find the frequency of number X from the given array.
list_ = [125,13,14,1,12,14,1,1,3,1]
# Step 1: Extract all digits from the numbers in the list
all_digits = []
for num in list_:
  for digit in str(num):
    all_digits.append(int(digit))

print(all_digits)

frequency = {}
for digit in all_digits:
  if digit in frequency:
    frequency[digit] +=1
  else:
    frequency[digit] = 1

most_common_digit = None
max_count = 0

for digit, count in frequency.items():
  if count > max_count:
    max_count = count
    most_common_digit = digit

print(frequency.items())


print(f"Most common digit is {most_common_digit} and it appeared {max_count} times")

# Write a program to find the frequency of number X from the given array.

numbers = [1,2,4,5,6,4,2,1,21,3,1,5,4,21,21,5,4,4,1,21,1,21,4,4,1,4,1,2,1,10,4]

freq = {}


for num in numbers:
  if num in freq:
    freq[num] += 1
  else:
    freq[num] = 1

# print(freq)
most_digits = None
max = 0

# python_frequency = {
#       1: 8, 
#       2: 3, 
#       4: 9, 
#       5: 3, 
#       6: 1, 
#       21: 5, 
#       3: 1, 
#       10: 1

#   }
for key, value in freq.items():
  if value > max:
    max = value
    most_digits = key

print(f"Most common digit is {most_digits} and it appeared {max}")


# Problem: remove duplicate numbers
list_of_num = [1,2,3,4.5,-3,5,5,4,2,3.5,4.5,-3,-2,5,6,8,5,2,4,5,21,2,5,6,5,6,5,65,5,6,54,65,20.1,21,0]
print(list_of_num)
new_list = []

for item in list_of_num:
  if item not in new_list:
    new_list.append(item)

print(new_list)


squares = [n**2 for n in range(10)]
print(squares)

for n in range(10):
  print(n*n,end=" ")
print()

sq = [n**4 for n in range(10)]
print(sq)






