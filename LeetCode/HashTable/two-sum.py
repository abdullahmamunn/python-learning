# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up 
# to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

 
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


# Solution with hashMap time complexity O(1)
class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in hash_map:
                return [hash_map[complement], index]
            hash_map[value] = index #store the value and index


# use nested loop  

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]


# find the single number in the list
array = [2, 2, 1]
# Output: 1
# Explanation: The number that occurs only once in the array is 1.

# Solution
# Using XOR operator

class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result
    
# using hash table
class Solution(object):
    def singleNumber(self, nums):
        hash_table = {}
        for num in nums:
            if num in hash_table:
                hash_table[num] += 1
            else:
                hash_table[num] = 1
        for key, value in hash_table.items():
            if value == 1:
                return key
            
# move zeros to the end of the list
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
example  = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Solution
# using two pointer

# move zeros to end 

def moveZerosToEnd(nums):
  left = 0
  for right in range(len(nums)):
    if nums[right] != 0:
      nums[left], nums[right] = nums[right], nums[left]
      left +=1
      
  return nums
    

nums = [0,1,0,3,12]    
print(moveZerosToEnd(nums))
  

# Input: [0,1,0,3,12]  
# Output: [1,3,12,0,0]
    

# First Missing Positive (Medium)
# Given an unsorted integer array nums, find the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses constant extra space.

# Example 1: 
# Input: [3,4,-1,1]  
# Output: 2
# Explanation: The smallest missing positive integer is 2.
# Solution
# using hash table

class Solution(object):
        def firstMissingPositive(self, nums):
            hash_table = {}
            for num in nums:
                hash_table[num] = 1
            for i in range(1, len(nums)+1):
                if i not in hash_table:
                    return i
            return len(nums)+1
        


# Maximum Subarray (Kadane’s Algorithm)
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Solution
# using Kadane’s Algorithm

class Solution(object):
    def maxSubArray(self, nums):
        current_sum = max_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum
    

# Find Second Largest Number in an Array

# Given an integer array, find the second largest element in it.
# Example 1: 
# Input: [10, 5, 8, 20,15]
# Output: 15

# Solution
# using sort

def second_largest(nums):
    nums.sort()
    return nums[-2]

# use two variable
def second_largest(nums):
    first = second = float('-inf')
    for num in nums:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second


# Input: [10, 5, 8, 20, 15]  
# Output: 15

# Check if an Array is a Subset of Another Array
# Given two integer arrays, nums1 and nums2, return true if nums1 is a subset of nums2.
# A subset is a set that contains all the elements of another set.

# Example 1: 
# Input: nums1 = [1,2,3], nums2 = [1,2,3,4,5]
# Output: True

# Solution
# using set

def isSubset(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return set1.issubset(set2)

# use hash table
def isSubset(nums1, nums2):
    hash_table = {}
    for num in nums1:
        hash_table[num] = 1
    for num in nums2:
        if num not in hash_table:
            return False
    return True 

# Find Intersection of Two Arrays

def intersection(nums1, nums2):
  hash_table = set(nums1)
  common = []
  

  for n in nums2:
    if n in hash_table:
      common.append(n)
      hash_table.remove(n)
      
  return common
 
  
nums1 = [1,2,2,1,3,4,5,6]
nums2 = [2,2,1,6]  
print(intersection(nums1, nums2))


# Find the Majority Element
# Use Boyer-Moore Voting Algorithm for O(n) time complexity.

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


