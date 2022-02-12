class Solution:
    def intToRoman(self, num: int) -> str:
        alp = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        ans, i = "", 0
        while(num > 0):
            rem = num % 10
            
            # 10^0  10^1  10^2 ...
            pos = pow(10, i)
            
            if rem == 4:
                # 4 as IV,  40 as XL , 400 as CD
                ans = alp[1*pos] + alp[5*pos] + ans
            elif rem == 9:
                # 9 as IX,  90 as XC , 900 as CM
                ans = alp[1*pos] + alp[10*pos] + ans
            elif rem >= 5:
                # bigger than five add 5, 50, 500... then rest
                ans = alp[5*pos]  + alp[1*pos] * (rem - 5) + ans
            else:
                # less than five add 1, 10, 100.. then rest
                ans = alp[1*pos] * rem + ans
            
            num = num // 10
            i += 1
            
        return ans

test = Solution()
print(test.intToRoman(1994)) # MCMXCIV