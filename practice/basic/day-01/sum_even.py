# Write a program to calculate the sum of all even numbers from 1 to
# Example:
# Input: 10
# Output: 30 (2 + 4 + 6 + 8 + 10)

def sum_of_even(n):

  sum = 0

  for num in range(1, n+1):
    if check_even(num):
       sum +=num
  return sum

def check_even(num):
  if num %2 ==0:
    return True
  

while True:

  n = int(input("Enter a number: "))
  res = sum_of_even(n)
  print(res)


