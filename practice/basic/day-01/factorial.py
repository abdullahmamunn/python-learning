# Write a program to calculate the factorial of a number using a while loop.
# Example
# Input: 5
# Output: 120

def calc_factorial(num):
  fact = 1
  steps = []
  for i in range(num, 0, -1):
    fact = fact * i
    steps.append(str(i))

  calculation = " x ".join(steps) + f" = {fact}"
  # print(calculation)
  return fact

for num in range(1, 11):
    print(f"{num}! = {calc_factorial(num)}")

# while True:
#   num = int(input("Enter a number: "))
#   res = calc_factorial(num)
  # print(res)
