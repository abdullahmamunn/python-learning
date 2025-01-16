n = int(input())
s = set(map(int, input().split()))
number = int(input())
for i in range(0,number):
    x = input().split()
    if x[0] == 'intersection_update':
        s.intersection_update(int(x[1]))
        print(s)