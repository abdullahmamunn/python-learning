def fibonacci_numbers(n):
  if n <=0:
    return []
  elif n == 1:
    return [0]
  elif n == 2:
    return [0,1]
  
  fibonacci = [0,1]
#  the underscore (_) is often used as a throwaway variable when the actual value is not 
# important or will not be used. It is a convention to indicate that the value is ignored.
  for _ in range(2, n): 
    next_num = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_num)
  return fibonacci

while True:
  n = int(input("Enter a number: "))

  res = fibonacci_numbers(n)
  print(res)
