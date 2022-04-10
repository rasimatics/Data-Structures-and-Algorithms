class Solution:
    def isValid(self, s: str) -> bool:        
        opened = {
          '(': ')',
          '{': '}',
          '[': ']'
        }
        
        stack = []
        
        for i in s:
            if i in opened:
                stack.append(i)
            else:
                if not stack or i != opened[stack.pop()]:
                    return False
                     
        return len(stack) == 0