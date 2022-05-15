class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def search(L, R):
            if L > R: return L
            M = (L + R) // 2
            
            if nums[M] < target:
                L = M + 1 
            elif nums[M] > target:
                R = M - 1
            else:
                return M
            return search(L, R)
        
        return search(0, len(nums) - 1)
    
    def searchInsert2(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        while L <= R:
            M = (L + R) // 2
            if nums[M] < target:
                L = M + 1 
            elif nums[M] > target:
                R = M - 1
            else:
                return M
        return L
        
        
    


            
        