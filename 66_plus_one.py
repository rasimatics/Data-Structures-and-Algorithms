from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1

        while carry == 1 and i >= 0:
            digits[i] += 1
            carry = 0
            if digits[i] == 10:
                carry = 1
                digits[i] = 0
            i -= 1
            
        if carry == 1:
            digits = [1] + digits
            
        return digits

            
test = Solution()

assert test.plusOne([1,2,9]) == [1, 3, 0]