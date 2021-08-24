from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        i = 0
        j = length -1
        n = length -1
        sorted = [None] * length

        while i <= j:
            if abs(nums[i]) < abs(nums[j]):
                sorted[n] = nums[j] * nums[j]
                j -= 1
            else:
                sorted[n] = nums[i] * nums[i]
                i += 1
           
            n -= 1

        return sorted


test1 = Solution()
print(test1.sortedSquares([-4, -1, 0, 3, 10])) # return [0, 1, 9, 16, 100]

