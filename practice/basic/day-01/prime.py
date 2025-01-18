def check_prime(number):
  if number <= 1:       # Numbers less than or equal to 1 are not prime
    return False
  
  for i in range(2, int(number ** 0.5) + 1):
    if number %i == 0:  # If divisible, it's not prime
      return False
  
  return True         # If no divisors found, it's prime


while True:

  num = int(input("Enter a number: "))
  if check_prime(num):
    print(f"{num} is prime")
  else:
    print(f"{num} is not prime")
  

