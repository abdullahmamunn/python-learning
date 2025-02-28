# A = [1, 2]
# B = [3, 4]
#
# AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
import itertools

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(*itertools.product(A,B))


