class Solution2:
    def bitwiseComplement(self, n: int) -> int:
        binary = list(self.convert_to_binary(n))
        for i in range(len(binary)):
            if binary[i] == '0':
                binary[i] = '1'
            else:
                binary[i] = '0'
                                
        return self.convert_to_dec("".join(binary))
    
    def convert_to_binary(self, n) -> str:
        if n <= 0: return "0"
    
        res = ""

        while n != 0:
            r = n % 2
            res = str(r) + res
            n = n // 2
        return res
    
    
    def convert_to_dec(self, binary):
        length = len(binary)

        res = 0

        for i in range(length):
            index = length - i - 1
            res += int(binary[index]) * pow(2, i)

        return res
    
    
    
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        mask = 1
        
        while mask < n:
            mask = (mask << 1) + 1
        
        return mask ^ n
 
