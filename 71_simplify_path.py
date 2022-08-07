class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        for i in path.split("/"):
            if i == '' or i == '.':
                continue
            elif i == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(i)
        
        result =""
        
        for i in stack:
            result += "/" + i
            
        return "/" if result == "" else result