from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        writePointer = 0
        
        for readPointer in range(len(nums)):
            if nums[readPointer] != 0:
                nums[writePointer] = nums[readPointer]
                writePointer += 1
        
        while writePointer < len(nums):
            nums[writePointer] = 0
            writePointer += 1
            
        