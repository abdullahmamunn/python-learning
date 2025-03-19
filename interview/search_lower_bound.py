def searchLowerBound(array, key):
    start_index = 0
    last_index = len(array) - 1
    while start_index <= last_index:
        mid = int((start_index + last_index)/2)
        if key == array[mid]:
            last_index = mid - 1
        elif key > array[mid]:
            start_index = mid + 1
        else:
            last_index = mid - 1

    return start_index


info = [100, 2, 10, 50, 20, 500, 100, 150, 200, 1000, 100]
info = sorted(info)

print(info)
while True:
    X = int(input())
    lowerbound = searchLowerBound(info, X)
    info.insert(lowerbound, X)
    print("New array ", info)
