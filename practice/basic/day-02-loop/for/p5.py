def calculate_factorial(n):
  fact = 1
  for i in range(n, 0, -1):
    fact *=i

  return fact

while True:
  x = int(input())
  res = calculate_factorial(x)

  print(res)
