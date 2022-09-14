class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.append(0)
        nums.sort()
        _sum = 0        
        
        
        def find_sum(start, end): 
            return  ((end + 1) * end - (start - 1) * start) // 2
        
        i = 0
        while  i < len(nums)-1:
            start = nums[i]
            end = nums[i + 1]
            i += 1
            
            delta = min(k, end - start - 1)
            if delta <= 0: continue
                
            _sum += find_sum(start+1, start + delta)
            
            k -= delta
            
        if k > 0:
            _sum += find_sum(nums[-1]+1, nums[-1] + k)
            
        return _sum
                
            
    
    # Time Limit Exceed
    def minimalKSum2(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        
        start = 1
        stop = heapq.heappop(nums)
        
        _count = 0
        _sum = 0
        
        while _count < k:
            if start < stop:
                _sum += start
                _count += 1
                start += 1
            elif nums:
                start = stop + 1
                stop = heapq.heappop(nums)
            else: break
            
            
        while _count < k:
            stop += 1
            _sum += stop 
            _count += 1
            
        
                
        return _sum
            
