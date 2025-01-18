# You will be given an input N, You have multiply B, P times.
# If B=2 and P=3 then the corresponding output is: 2*2*2=8

def calculate_power(base, power):
  result = 1
  for _ in range(power):
    result = result * base
  # res = base ** power
  return result


while True:
  base = int(input())
  power = int(input())

  res = calculate_power(base, power)

  print(res)
