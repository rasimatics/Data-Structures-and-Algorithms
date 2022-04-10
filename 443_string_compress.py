class Solution:    
    def compress(self, chars: List[str]) -> int:
        index, iterator = 0, 0
        
        while iterator < len(chars):
            chars[index] = chars[iterator]
            count = 1
            
            while iterator + 1 < len(chars) and chars[iterator] == chars[iterator + 1]:
                iterator += 1
                count += 1
            
            if count > 1:
                for i in str(count):
                    chars[index + 1] = i
                    index += 1
            index += 1
            iterator += 1
        
        return index
    
        
    def compress_my_solution(self, chars: List[str]) -> int:
        s = ""
        counter = 1
        
#       Count and add to s
        for i in range(0, len(chars) - 1):
            if chars[i] == chars[i + 1]:
                counter += 1
            else:
                s += chars[i]
                if counter > 1: s += str(counter)
                counter = 1
        
        if counter > 1:
            s += chars[-1]
            s += str(counter)
        else:
            s += chars[-1]
        
#       Modify chars array
        i = 0
        for char in s:
            chars[i] = char
            i += 1
        
        chars = chars[:i]
        return len(chars)
                
                    