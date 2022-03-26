from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_first = 0
        max_first_index = 0
        max_second = 0
        
        for index, value in enumerate(nums):
            if value > max_first:
                max_second = max_first
                max_first = value
                max_first_index = index
            elif value > max_second:
                max_second = value
                
        return max_first_index if max_second * 2 <= max_first else -1


test = Solution()
assert test.dominantIndex([3,6,1,0]) == 1