from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_c = 0
        
        for i in nums:
            if i == 1:
                counter += 1
            else:
                max_c = max(max_c, counter)                
                counter = 0
        return max(max_c, counter)  


test1 = Solution() 
print(test1.findMaxConsecutiveOnes([1,1,0,1,1,1])) # return 3