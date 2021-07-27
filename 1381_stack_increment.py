class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        

    def push(self, x: int) -> None:
        if self.stack_len() != self.maxSize:
            self.stack.append(x)
        

    def pop(self) -> int:
        if self.stack_len() > 0:
            top = self.stack.pop()
            return top
        return -1
        

    def increment(self, k: int, val: int) -> None:
        iteration = k if k < self.stack_len() else self.stack_len()
        
        for i in range(iteration):
            self.stack[i] += val


    def stack_len(self):
        return len(self.stack)

        
customStack = CustomStack(3)                 # Stack is Empty []
customStack.push(1)                          # stack becomes [1]
print(customStack.stack)
customStack.push(2)                          # stack becomes [1, 2]
print(customStack.stack)
print(customStack.pop())                     # return 2 --> Return top of the stack 2, stack becomes [1]
customStack.push(2)                          # stack becomes [1, 2]
print(customStack.stack)
customStack.push(3)                          # stack becomes [1, 2, 3]
print(customStack.stack)
customStack.push(4)                          # stack still [1, 2, 3], Don't add another elements as size is 4
print(customStack.stack)
customStack.increment(5, 100)                # stack becomes [101, 102, 103]
print(customStack.stack)
customStack.increment(2, 100)                # stack becomes [201, 202, 103]
print(customStack.stack)
print(customStack.pop())                     # return 103 --> Return top of the stack 103, stack becomes [201, 202]
print(customStack.pop())                     # return 202 --> Return top of the stack 102, stack becomes [201]
print(customStack.pop())                     # return 201 --> Return top of the stack 101, stack becomes []
print(customStack.pop())                     # return -1 --> Stack is empty return -1.