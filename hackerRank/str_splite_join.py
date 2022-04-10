# s = input().split(" ")
# s = "-".join(s)
# print(s)

def split_and_join(line):
    # write your code here
    line = "-".join(line)
    return line


if __name__ == '__main__':
    line = input().split(" ")
    result = split_and_join(line)
    print(result)