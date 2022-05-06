class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0: return 0
        return 9 if num % 9 == 0 else num % 9
    
    def addDigits2(self, num: int) -> int:
        while num > 9:
            new_num = 0
            while num > 0:
                new_num += num % 10
                num = num // 10
            num = new_num
        
        return num