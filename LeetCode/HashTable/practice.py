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
def moveZeroes(nums):
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


# Rotate Array by k steps
def rotate(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums

# exmaple
nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums, k)) # [5,6,7,1,2,3,4]
# using loop
def rotate(nums, k):
    for i in range(len(nums) - k):
        nums.insert(0, nums.pop())
        return nums
    
# exmaple
nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums, k)) # [5,6,7,1,2,3,4]


# Find the First Unique Character in a String
def firstUniqChar(s):
    hash_table = {}
    for char in s:
        hash_table[char] = hash_table.get(char, 0) + 1
        
    for i, char in enumerate(s):
        if hash_table[char] == 1:
            return i
    return -1

# in php 
# function firstUniqChar($s) {
#     $hash_table = [];
#     for($i = 0; $i < strlen($s); $i++){
#         $hash_table[$s[$i]] = ($hash_table[$s[$i]] ?? 0) + 1;
#     }
#     for($i = 0; $i < strlen($s); $i++){
#         if($hash_table[$s[$i]] == 1){
#             return $i;
#         }
#     }
#     return -1;
# }

