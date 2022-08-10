class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        store = [1] * n
        
        for i in range(n-1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    store[i] = max(store[i], 1 + store[j])
                    
        return max(store)