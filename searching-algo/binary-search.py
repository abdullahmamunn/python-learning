# Implementing binary search
#define function binary search

def binarySearch(arr, target_item):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target_item:
            return mid
        elif arr[mid] < target_item:
            left = mid + 1
        else:
            right = mid - 1
    return -1


array = [12,1,10,15,12,15,5,13,11,20]
array.sort()
print(array)
while True:
    key = int(input())
    res = binarySearch(array,key)
    if res != -1:
        print(f"Element found in index {res}")
    else:
        print("Element not found")

