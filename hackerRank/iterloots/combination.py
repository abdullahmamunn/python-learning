import itertools
x = input().split()
res = itertools.combinations(x[0],int(x[1]))
for item in sorted(res):
    print("".join(item))
