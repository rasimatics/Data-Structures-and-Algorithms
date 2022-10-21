class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        _dict = {}
        
        for index, value in enumerate(nums):
            if value in _dict:
                if abs(_dict[value] - index) <= k:
                    return True
            _dict[value] = index
                
        return False
            
