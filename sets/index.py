# basic learning set
set_a = {5, 1, 2, 3, 4, 2, 3,1}
set_b = set((5, 5, 7, 3, 10, 11, 12, 9, 8))
print(set_b)
print(set_a)
for set_items in set_b:
    print(set_items)

set_union = set_a.union(set_b)
set_union = set_a | set_b

set_intersection = set_a.intersection(set_b)
set_intersection = set_a & set_b

set_dif = set_b.difference(set_a)
set_dif = set_b - set_a

set_symntc = set_a.symmetric_difference(set_b)
set_symntc = set_a ^ set_b

print(set_union)
print(set_intersection)
print(set_dif)
print(set_symntc)

A = set(("Mamun", "mamun", "mita", 123354354, "abdullah", "tutul"))
B = set(("shuvo", "mamun", "mitu", 213, "abdullah", "tutul"))
print(A - B)
print(A | B)
print(A & B)
print(A ^ B)
