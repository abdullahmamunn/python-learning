n = int(input())

binary = []
while n>0:
    remainder = n%2
    n = n//2
    binary.append(remainder)
binary.reverse()
cnt = 0
mx = 0
for numbers in binary:
    if numbers == 1:
        cnt +=1
        if cnt>mx:
            mx = cnt
    else:
        cnt = 0
print(mx)

