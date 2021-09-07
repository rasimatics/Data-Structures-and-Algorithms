from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_index = 0
        odd_index = len(nums) - 1
        final_arr = [None] * len(nums)
        
        for i in nums:
            if i % 2 == 0:
                final_arr[even_index] = i
                even_index += 1
            else:
                final_arr[odd_index] = i
                odd_index -= 1
                
        return final_arr