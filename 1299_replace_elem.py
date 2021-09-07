from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_in_right = arr[len(arr) - 1]
        i = len(arr) - 2

        while i >= 0:
            temp = arr[i]
            arr[i] = max_in_right 

            if temp > max_in_right:
                max_in_right = temp
             
            i -= 1
        
        arr[-1] = -1 

        return arr


test = Solution()
print(test.replaceElements([17,18,5,4,6,1]))