even_array = list()
odd_array = list()
ar = [1,2,3,4,5,6,7,8,9,10]

even_sum = 0;
odd_sum = 0;

for num in ar:
  if num%2 == 0:
    even_sum = even_sum + num
    even_array.append(num)
  else:
    odd_sum = odd_sum + num
    odd_array.append(num)


print(f"Even array: {even_array}")
print(f"Even Sum is: {even_sum}")

print()

print(f"Odd array: {odd_array}")
print(f"Odd Sum is: {odd_sum}")
