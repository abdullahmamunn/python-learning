def find_sinle_number(nums):
  
  hash_table = {}
  
  for n in nums:
    if n in hash_table:
      hash_table[n] +=1
    else:
      hash_table[n] = 1 
      
  
  for key, value in hash_table.items():
    if value == 1:
      return key


nums = [4,1,2,1,2]  
print(find_sinle_number(nums)) # 4


# Move Zeros to end
def moveZeroes(self, nums):
    L = 0
    for R in range(len(nums)):
        if nums[R] !=0:
            nums[L], nums[R] = nums[R], nums[L]
            L+=1
    return nums

# First Missing Positive

def firstMissingPositive(nums):
    hash_table = {}
    for num in nums:
        hash_table[num] = 1
    
    for i in range(1, len(nums) + 1):
        if i not in hash_table:
            return i
        
    return len(nums) + 1


# Maximum Subarray (Kadane’s Algorithm)
def maxSubArray(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
        
    return max_sum
