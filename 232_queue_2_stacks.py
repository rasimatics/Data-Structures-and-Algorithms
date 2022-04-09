class MyQueue:

    def __init__(self):
        self.pop_stack = []
        self.push_stack = []
        

    def push(self, x: int) -> None:
        self.push_stack.append(x)
        

    def pop(self) -> int:
        if self.pop_stack:
            return self.pop_stack.pop()
        
        while self.push_stack:
            self.pop_stack.append(self.push_stack.pop())
        
        return self.pop_stack.pop()

    
    def peek(self) -> int:
        if self.pop_stack:
            return self.pop_stack[-1]
        return self.push_stack[0]

        
    def empty(self) -> bool:
        return not(self.push_stack or self.pop_stack)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()