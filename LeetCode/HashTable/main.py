def majorityElement(nums):
    count = 0
    selected_num = None

    for num in nums:
        if count == 0:
            selected_num = num
        
        if selected_num == num:
            count +=1
        else:
            count -=1
    return selected_num

# Input: [0,3,4,2,3,3,3] 
    

nums = [0, 2, 4, 2, 0, 3, 0, 1,2]
print(majorityElement(nums))  # Output: 3
