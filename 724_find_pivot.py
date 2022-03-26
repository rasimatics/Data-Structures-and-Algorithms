from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = 0
        for i in nums:
            total_sum += i
        
        left_sum = 0
        for i in range(len(nums)):
            if left_sum == total_sum - left_sum - nums[i]:
                return i
            left_sum += nums[i]
        return -1
        

test = Solution()

assert test.pivotIndex([1,7,3,6,5,6]) == 3