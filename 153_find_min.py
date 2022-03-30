from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0: return -1
        if len(nums) == 1: return nums[0]
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + int((right - left) / 2)
            
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[left] <= nums[mid] and nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
                
        return nums[left]
    