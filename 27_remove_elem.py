from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        final_length = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
                final_length += 1
        return final_length
        

test1 = Solution()
print(test1.removeElement([2], 3))
