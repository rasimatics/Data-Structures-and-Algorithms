class Solution:
    def reverseParentheses(self, s: str) -> str:
        current = ""
        stack = []
        
        for i in s:
            if i == "(":
                stack.append(current)
                current = ""
            elif i == ")":
                current = stack.pop() + current[::-1]
            else:
                current += i
        return current


test = Solution()
print(test.reverseParentheses("(u(love)i)"))
print(test.reverseParentheses("(ed(et(oc))el)"))