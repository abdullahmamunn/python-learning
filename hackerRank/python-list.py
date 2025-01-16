if __name__ == '__main__':
    N = int(input())
    my_list = [];
    for i in range(0,N):
        command = input().split()
        if command[0] == "insert":
             index = int(command[1])
             value = int(command[2])
             my_list.insert(index,value)
        elif command[0] == "remove":
             value = int(command[1])
             my_list.remove(value)
        elif command[0] == "append":
             value = int(command[1])
             my_list.append(value)
        elif command[0] == 'sort':
             my_list.sort()
        elif command[0] == "pop":
             my_list.pop()
        elif command[0] == "reverse":
             my_list.reverse()
        elif command[0] == "print":
             print(my_list)
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
