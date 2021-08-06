class Stack:
    def __init__(self):
        self.list = []
        
    def push(self, val):
        self.list.append(val)
        
    def pop(self):
        return self.list.pop()
    
    def size(self):
        return len(self.list)
    
    def clear(self):
        self.list.clear()
    
    def is_empty(self):
        return self.size() == 0

    
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = Stack()
        self.stack2 = Stack()
        
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.push(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.empty():
            for _ in range(self.stack1.size() - 1):
                self.stack2.push(self.stack1.pop())

            elem = self.stack1.pop()

            self.stack1.list = list(self.stack2.list[::-1])
            self.stack2.clear()

            return elem
        return -1
            

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.empty():
            for _ in range(self.stack1.size() - 1):
                self.stack2.push(self.stack1.pop())

            elem = self.stack1.pop()

            self.stack1.list = list([elem] + self.stack2.list[::-1])
            self.stack2.clear()

            return elem
        return -1
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.stack1.is_empty()
        

myQueue = MyQueue() 
myQueue.push(1)
myQueue.push(2)
myQueue.push(3)
myQueue.push(4)
print(myQueue.stack1.list)
print(myQueue.pop())
myQueue.push(5)
print(myQueue.stack1.list)
print(myQueue.pop())
print(myQueue.pop())
print(myQueue.pop())
print(myQueue.pop())
