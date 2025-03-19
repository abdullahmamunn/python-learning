def linerSearch(arr,search_item):
    for i in range(len(arr)):
        if arr[i] == search_item:
            return i
    
    return -1

age = [10,15,50,20,30,25,19]
key = 190
print(age)
while True:
    key = int(input())
    result = linerSearch(age,key)

    if result != -1:
        print(f"Item is found at position {result}")
    else:
        print("Item Not found!")
