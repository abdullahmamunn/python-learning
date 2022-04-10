if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    set_a = set(arr)

    n = int(input())
    arr = list(map(int, input().split()))
    set_b = set(arr)
    res = set_a.symmetric_difference(set_b)
    sorted_set = sorted(res)
    for item in sorted_set:
        print(item)
