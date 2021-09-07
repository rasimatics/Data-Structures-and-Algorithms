from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()

        for i in arr:
            if i*2 in s or i/2 in s:
                return True
            else:
                s.add(i)
        return False
        
        



test1 = Solution()
print(test1.checkIfExist([3,1,7,11]))   # false
print(test1.checkIfExist([7,1,14,11]))  # true
