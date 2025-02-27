def average(array):
     set_items = set(array)
     return  sum(set_items)/len(set_items)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)