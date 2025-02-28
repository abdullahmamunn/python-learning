# print 1 to n without loop
def print_num(i,n):
    if i>n:
        return
    print(i)
    print_num(i + 1, n)

n = 10
print_num(1,n)


n
