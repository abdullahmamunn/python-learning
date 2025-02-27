# You will be given an input N, You have to print the sum of the series.
# If N=6 then the corresponding output is: 1-2+3-4+5-6=-3

def calculate_series_of_sum(num):
  total = 0
  for i in range(1, num + 1):
    if i%2 == 1:
      total = total + i
    else:
      total = total - i

  return total

while True:
  x = int(input())
  res = calculate_series_of_sum(x)
  print(res)
