from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = nums[0]
        
        for i in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += i
            max_sum = max(cur_sum, max_sum)
        
        return max_sum