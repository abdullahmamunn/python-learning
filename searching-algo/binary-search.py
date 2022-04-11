def binarySearch(arr,key):
    left = 0
    right = len(arr)-1
    index = None
    while left <= right:
        mid = int((left + right)/2)
        if key == arr[mid]:
            index = mid
            break
        elif key > arr[mid]:
             left = mid + 1
        elif key < arr[mid]:
            right = mid - 1
    return index



age = [10,15,50,20,30,25,19]
age.sort()
print(age)
while True:
    key = int(input())
    index = binarySearch(age,key)
    print(index)
