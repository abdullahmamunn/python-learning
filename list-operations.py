
# x = list(map(int, input().split()))
# print(x)
# print(type(x))
x = list(map(int, input().split()))
print(type(x))
# sort the list
x.sort()
print(x)
max_value = x[-1]
min_value = x[0]
print(max_value)
print(min_value)
print(max_value+min_value)
# value, index = input().split()
# print(value,index)
# x.insert(int(value),int(index))
print(x)

# linear searching
find = int(input())
for item in x:
    if find == item:
        print(x[find])