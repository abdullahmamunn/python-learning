
# def check_prime(number):
#   if number <= 1:       # Numbers less than or equal to 1 are not prime
#     return False
  
#   for i in range(2, int(number ** 0.5) + 1):
#     if number %i == 0:  # If divisible, it's not prime
#       return False
  
#   return True         # If no divisors found, it's prime

# def print_prime_upto_n(n):
#   print(f"Print prime number upto {n}")
#   counter = 0;
#   for num in range(2, n+1):  # Start from 2, as 1 is not prime
#     if check_prime(num):
#       print(num, end=" ")
#       counter +=1
#   print(f"\nTotal Prime numbers found {counter} between 1 to {n}")

# while True:

#   num = int(input("Enter a number: "))
#   print_prime_upto_n(num)


def check_prime(number):
  if number <= 1:       # Numbers less than or equal to 1 are not prime
    return False
  
  for i in range(2, int(number ** 0.5) + 1):
    if number %i == 0:  # If divisible, it's not prime
      return False
  
  return True         # If no divisors found, it's prime

def print_prime_upto_n(start, end):
  print(f"Prime numbers between {start} and {end}:")
  counter = 0;
  for num in range(start, end+1):  # Start from 2, as 1 is not prime
    if check_prime(num):
      print(num, end=" ")
      counter +=1
  print(f"\nTotal Prime numbers found {counter}")

while True:

  start, end = map(int, input("Enter start and end numbers (separated by a space): ").split())
  if start < 2:  # Adjusting condition for start number
      print(f"Start number must be greater than or equal to 2.")
  elif end <= start:  # Ensuring end is greater than start
      print(f"End number must be greater than start number.")
  else:
      print_prime_upto_n(start, end)
      break  # Exit the loop after successful execution


