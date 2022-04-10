# Find maximum number in a list
numbers = [int(x) for x in input().split()]
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print("Max is " + str(maximum))

# Sort a list
numbers.sort()
print(numbers)
min_sum = 0;
for item in numbers[0:4]:
    min_sum += item
print(min_sum)
max_sum = 0
for item in numbers[1:5]:
    max_sum += item
print(max_sum)

