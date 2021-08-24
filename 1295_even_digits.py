from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        
        return count



test1 = Solution() 
print(test1.findNumbers([555,901,482,1771])) # return 1