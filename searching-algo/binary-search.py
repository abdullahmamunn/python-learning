# Implementing binary search
#define function binary search

<<<<<<< HEAD
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
=======
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
>>>>>>> a99467d3999b629e0eeb62b72972a9412ad25923
array.sort()
print(array)
while True:
    key = int(input())
    res = binarySearch(array,key)
<<<<<<< HEAD
    print(res)
=======
    if res != -1:
        print(f"Element found in index {res}")
    else:
        print("Element not found")
>>>>>>> a99467d3999b629e0eeb62b72972a9412ad25923

