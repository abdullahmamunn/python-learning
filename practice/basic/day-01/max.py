# Write a program to find the largest number in a list.

# example:
# Input: [3, 7, 2, 8, 5]
# Output: 8

def find_max(numbers):
  max = 0
  for num in numbers:
    if num > max:
      max = num
  
  return max

while True:
  
  numbers = [float(n) for n in input("Enter your list: ").split()]
  max_num = find_max(numbers)
  print(f"Max number is {max_num}")
