from typing import List

class Solution:
    
#    time - O(n) space - O(1)
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
                
        
        for i in range(len(nums)):
            curr = abs(nums[i])
            
            if 1 <= curr <= len(nums):
                if nums[curr - 1] > 0:
                    nums[curr - 1] *= -1
                elif nums[curr - 1] == 0:
                    nums[curr - 1] = -(len(nums) + 1)
        
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        
        return len(nums) + 1

    
#   time - O(n)  space - O(n)
    def firstMissingPositive2(self, nums: List[int]) -> int:
        num_dict = {}
        
        for i in nums:
            num_dict[i] = 1
            
        for i in range(1, len(nums) + 2):
            if i in num_dict:
                continue
            else:
                return i
            
