if __name__ == '__main__':
    ls = []
    for _ in range(0,int(input())):
        name = input()
        score = float(input())
        ls.append([name,score])
marks = []
for i in range(0, len(ls)):
    for j in range(0, 2):
        if j == 1:
            marks.append(ls[i][j])
    # print(lowest)
marks.sort()
print(marks)
print(marks[1])
l = marks[0]
for mark in marks:
    if mark == l:
        continue;
    else:
        second_l = mark
        break

print(second_l)
names = []
for res in ls:
    if res[1] == second_l:
        # print(res[0])
        names.append(res[0])
names.sort()
for name in names:
    print(name)


# lls = [
#     ['Harry', 37.21],
#     ['Berry', 37.21],
#     ['Berry', 37.15],
#     ['Tina', 37.2],
#     ['Akriti', 41],
#     ['Harsh', 39]
# ]
# print(lls[0][1])
# print(lls[1][1])
# print(lls[2][1])
# print(lls[3][1])





