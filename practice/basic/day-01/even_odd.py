# Write a program that checks whether a given number is odd or even.
# Example:
# Input: 4
# Output: Even

def check_even_odd(num):
  if num %2 == 0:
    return "Even"
  else:
    return "odd"

while True:

  number = int(input("Enter a integer number: "))

  res = check_even_odd(number)
  print(f"Number {number} is {res}")
