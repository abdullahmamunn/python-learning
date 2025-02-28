dic = {}
n = int(input())
for yo in range(n):
    name, age, sex = input().split()
    dic[int(age)] = name, sex

# print(sorted(dic))

for key, value in sorted(dic.items()):
    if value[1] == 'M':
        print(f'Mr. {value[0]}')
    else:
        print(f'Ms. {value[0]}')
#	print(value[0])