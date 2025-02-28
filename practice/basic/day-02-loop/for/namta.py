def Namta(num):
  for i in range(1, 11):
    print(f"{i} x {num} = {i*num}")
  print()


while True:
  num = int(input())
  Namta(num)

