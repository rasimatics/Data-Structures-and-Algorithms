from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        
        for i in nums:
            if counter.get(i):
                return True
            counter[i] = 1
        return False