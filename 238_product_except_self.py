from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)        
        
        left_product = 1
        right_product = 1
        
#       left products
        for i in range(len(nums)):
            res[i] = left_product
            left_product *= nums[i]
            
#       right products
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]
            
        return res
            