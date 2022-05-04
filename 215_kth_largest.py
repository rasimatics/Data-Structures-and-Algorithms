class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k  # it gives index of kth largest
        
        def quickselect(l, r):
            p, pivot = l, nums[r]
            
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            
            nums[p], nums[r] = nums[r], nums[p]
            
            if k < p: return quickselect(0, p - 1)
            elif k > p: return quickselect(p + 1, r)
            else: return nums[p]
        
        return quickselect(0, len(nums) - 1)
        
        
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        
        while len(nums) > k:
            heapq.heappop(nums)
            
        return nums[0]