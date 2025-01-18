# Problem: Write a program that prints the multiplication table for any given number up to 10.

def print_multiplication_table(num):

  # print("Multiplication Table for number: {0}".format(num))
  print(f"Multiplication Table for number: {num}")

  for i in range(1,11):
    print(f"{num} X {i} = {num*i}")


num = int(input())
print_multiplication_table(num)

