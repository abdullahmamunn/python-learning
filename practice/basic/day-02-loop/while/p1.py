def find_sum_of_n(n):
  sum = 0;
  i = 1;
  while i <= n:
    sum +=i
    i+=1
  return sum


while True:
  num = int(input())
  n = find_sum_of_n(num)
  print(n)



