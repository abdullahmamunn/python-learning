# # Find maximum number in a list
numbers = [int(x) for x in input().split()]

# Sort a list
numbers.sort()
min_sum = 0;
for item in numbers[0:4]:
    min_sum += item
max_sum = 0
for item in numbers[1:5]:
    max_sum += item
print(min_sum,max_sum)


# Find maximum number in a list
numbers = [int(x) for x in input().split()]

# Sort a list
numbers.sort()
min_sum = sum(numbers[0:4])
max_sum = sum(numbers[1:5])
print(min_sum,max_sum)



# Transfer to function

def minimaxsum(num):
    num.sort()
    min_sum = sum(num[0:4])
    max_sum = sum(num[1:5])
    # print(min_sum,max_sum)
    return min_sum,max_sum


def main():
    numbers = list(map(int, input().rstrip().split()))
    print(minimaxsum(numbers))


if __name__ == '__main__':
    main()

