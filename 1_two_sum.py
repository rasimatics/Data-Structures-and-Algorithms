from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        
        for i, first_num in enumerate(nums):
            second_num = target - first_num
            if second_num in nums_dict:
                second_index = nums_dict[second_num]
                return [second_index, i]
            nums_dict[first_num] = i
        

test = Solution()
print(test.twoSum([3,2,4], 6)) # [1,2]