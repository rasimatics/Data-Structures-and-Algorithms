class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        final_len = 0
        curr_len = 0
        
        for i in nums:
            if (i + 1) not in num_set:
                curr_value = i
                curr_len = 1
                
                while (curr_value - 1) in num_set:
                    curr_len += 1
                    curr_value -= 1
            
            final_len = max(final_len, curr_len)
            
        return final_len
    
    # first solution
    def longestConsecutive2(self, nums: List[int]) -> int:
        _dict = {}
        
        for i in nums:
            if i not in _dict:
                _dict[i] = 0
        
        final_len = 0
        for i in nums:
            curr_len = 1
            
            _i = i
            while (_i + 1) in _dict:
                curr_len += 1
                _dict.pop(_i+1)
                _i = _i + 1
            
            _i = i
            while (_i - 1) in _dict:
                curr_len += 1
                _dict.pop(_i-1)
                _i = _i - 1
                
            final_len = max(final_len, curr_len)
            
        return final_len