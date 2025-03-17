# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Explanation:
# The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Explanation:
# All elements are distinct.

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true


# Solution : 01

def containsDuplicate(self, nums):
    original_length = len(nums)
    remove_duplicate = len(set(nums))

    if(original_length == remove_duplicate):
        return False
    else:
        return True


class Solution(object):
    def containsDuplicate(self, nums):
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return True
            
            hash_set.add(num)
        
        return False

  
class Solution(object):
    def containsDuplicate(self, nums):
        hash_table = {}
        for num in nums:
            if num in hash_table:
                return True
            
            hash_table[num] = 1
        
        return False