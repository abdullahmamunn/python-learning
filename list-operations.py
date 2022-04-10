
x = list(map(int, input().split()))
# print(x)
# print(type(x))
# x = [map(int, input().split())]
# print(type(x))
# sort the list
x.sort()
print(x)
value, index = input().split()
print(value,index)
x.insert(int(value),int(index))
print(x)

