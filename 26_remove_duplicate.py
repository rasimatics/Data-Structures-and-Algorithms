from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        for i in range(1, len(nums)):
            if nums[index - 1] != nums[i]:
                nums[index] = nums[i]
                index += 1
        return index




test1 = Solution()
print(test1.removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # return  length->5  list-> [0,1,2,3,4,_,_,_,_,_]

"""
    [0,0,1,1,1,2,2,3,3,4]   ->  [0,1,2,3,4,_,_,_,_,_]
    [0,1,1,1,1,2,2,3,3,4]
"""