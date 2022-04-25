
def arrays(arr):
    # return arr[::-1]
    return  [ar for ar in reversed(arr)]



arr = [1, 2, 3, 4, -8, -10]
result = arrays(arr)
print(result)