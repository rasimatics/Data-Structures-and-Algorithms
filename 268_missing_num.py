from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        
        total_sum = int((1 + length)/2 * length)
        
        cur_sum = 0
        for i in nums:
            cur_sum += i
            
        return total_sum - cur_sum