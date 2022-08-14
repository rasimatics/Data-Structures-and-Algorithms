class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        _dict = {0 : -1}
        mod = 0
        
        for i, num in enumerate(nums):
            mod = (mod + num) % k
            
            if mod not in _dict:
                _dict[mod] = i
            elif i - _dict[mod] > 1:
                return True
            
        return False
    
#   TLE solution (first try)

    def checkSubarraySum2(self, nums: List[int], k: int) -> bool:
        for i in range(2, len(nums) + 1):
            j = 0
            while j < len(nums):
                arr = nums[j:j+i]
                if len(arr) >= 2 and sum(arr) % k == 0:
                    return True
                j += 1
        return False
            
            
                