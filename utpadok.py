num = 1331 * 16807
print(num)
count = 0
for i in range(1, num+1):
    if num % i == 0:
        count += 1
        print(i)
print("Total count = {0}".format(count))