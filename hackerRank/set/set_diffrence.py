n = int(input())
set_1 = set(map(int, input().split()))
n = int(input())
set_2 = set(map(int, input().split()))
res = set_1.difference(set_2)
print(len(res))