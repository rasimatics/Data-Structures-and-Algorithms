from typing import Container, List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        else:
            last_number = arr[0]
            decreased_started = False

            for i in range(1, len(arr)):

                if not decreased_started:
                    if arr[i] > last_number:
                        last_number = arr[i]
                        continue
                    elif arr[i] == last_number or i == 1:
                            return False

                    decreased_started = True
                    last_number = arr[i]

                elif arr[i] < last_number:
                    last_number = arr[i]
                    continue
                else:
                    return False
            
            return  True if decreased_started else False          

test = Solution()
print(test.validMountainArray([0,3,2,1]))             # true
print(test.validMountainArray([3,7,20,14,15,14,10,8,2,1]))   # false