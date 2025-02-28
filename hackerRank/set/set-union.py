# a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# b = {10, 1, 2, 3, 11, 21, 55, 6, 8}
# c = a.union(b)
# print(len(c))
n = int(input())
set_1 = set(map(int, input().split()))
n = int(input())
set_2 = set(map(int, input().split()))
res = set_1.union(set_2)
print(len(res))

