from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)

        count = 0
        i = 0
        while i < len(heights):
            if expected[i] != heights[i]:
                count += 1
            i += 1

        return count

test = Solution()
print(test.heightChecker([1,1,4,2,1,3]))


# heights  = [1,1,4,2,1,3] 
# expected = [1,1,1,2,3,4]
# output   = 3
