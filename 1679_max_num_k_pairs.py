class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        
        while l < r:
            if nums[l] + nums[r] < k:
                l += 1
            elif nums[l] + nums[r] > k:
                r -= 1
            else:
                l += 1
                r -= 1
                res += 1
        
        return res
                
        
    def maxOperations2(self, nums: List[int], k: int) -> int:
        my_dict = {}
        res = 0
        
        for i in nums:
            my_dict[i] = my_dict.get(i, 0) + 1
        
        for i in nums:
            target = k - i
            
            if i == target and my_dict.get(target) < 2:
                continue
            
            if my_dict.get(target) and my_dict.get(target) > 0 and my_dict.get(i) > 0:
                my_dict[i] -= 1
                my_dict[target] -= 1
                res += 1
        
        return res
            