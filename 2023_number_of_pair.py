from typing import List

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        numDict = {}
        count = 0
        for i in nums:
            numDict[i] = numDict[i] + 1 if i in numDict else 1
        
        for i in range(len(target)):
            prefix = target[:i]
            suffix = target[i:] 
            
            if suffix in numDict and prefix in numDict:
                if suffix == prefix:
                    count += numDict[suffix] * (numDict[prefix] - 1)
                else:
                    count += numDict[suffix] * numDict[prefix]
                
        return count
                
test = Solution()
assert test.numOfPairs(["123","4","12","34"], "1234") == 2
assert test.numOfPairs(["777","7","77","77"], "7777") == 4