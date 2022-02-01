from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        medians = []
        for i in range(len(nums) - k + 1):
            current_nums = sorted(nums[i:i+k])
            medians.append(self.findMedian(current_nums))
        return medians
            
    def findMedian(self, nums: List[int]):
        if(len(nums) % 2 == 0):
            return (nums[len(nums)//2 - 1] + nums[len(nums)//2])/2
        return nums[len(nums)//2]
        

test = Solution()
print(test.medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3))