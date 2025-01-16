# Implementing binary search
#define function binary search

def binarySearch(array,key):
    start_index = 0
    last_index = len(array)-1
    index = None
    while start_index <= last_index:
        mid = int((start_index + last_index) /2)
        if key == array[mid]:
            index = mid
            last_index = mid - 1
        elif key > array[mid]:
            start_index = mid + 1
        else:
            last_index = mid - 1
    return index


array = [12,10,10,15,12,15,5,11,11,20]
array.sort()
print(array)
while True:
    key = int(input())
    res = binarySearch(array,key)
    print(res)

