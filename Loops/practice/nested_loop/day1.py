n = int(input())
for i in range(1,n+1):
    dec_num = i
    for dec_num in range(dec_num,0,-1):
        print(dec_num, end='')
        dec_num = dec_num - 1
    inc_num = 2
    for inc_num in range(inc_num,i+1):
        print(inc_num, end='')
        inc_num = inc_num + 1

    print()
# 1
# 212
# 32123
# 4321234
# Look at the problem we find two pattern from second line, that is increment and decrement here one loop is using for
# decrement like 21, 321,4321 and another one is fon
# incremenr like 2, 23, 234 and increment loop is started form 2
# NT: I found the idea from https://pyra idinpython.blogspot.com/2020/07/pyramid-number-pattern-print-following.html