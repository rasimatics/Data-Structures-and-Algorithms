class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        start, mid, end = 0, 0, len(nums) - 1
        
        while mid <= end:
            if nums[mid] == 0:
                nums[mid], nums[start] = nums[start], nums[mid]
                start += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
                
            else: # nums[mid] == 2
                nums[mid], nums[end] = nums[end], nums[mid]
                end -= 1