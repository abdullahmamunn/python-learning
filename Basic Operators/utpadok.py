# Find the Utpadok for the biggest number
num = 1331 * 16807
print(num)
count = 0
for i in range(1, num+1):
    if num % i == 0:
        count += 1
        print(i)
print("Total count = {0}".format(count))

"""
Output:
22370117
1
7
11
49
77
121
343
539
847
1331
2401
3773
5929
9317
16807
26411
41503
65219
184877
290521
456533
2033647
3195731
22370117
Total count = 24

Process finished with exit code 0


"""