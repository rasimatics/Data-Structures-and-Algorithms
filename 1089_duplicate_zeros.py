from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        new_arr = []
        for i in range(len(arr)):
            new_arr.append(arr[i])
            if arr[i] == 0:
                new_arr.append(0)

        # arr[:] copy of my arr not reference :)
        arr[:] = new_arr[:len(arr)]

        

test1 = Solution()
test1.duplicateZeros([1,0,2,3,0,4,5,0])
        