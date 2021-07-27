class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        return self.queue.append(element)
    
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        return None

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return self.size() == 0
    
    
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Queue1 = Queue()
        self.Queue2 = Queue()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.Queue1.enqueue(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        for i in range(0, self.Queue1.size() - 1):
            elem = self.Queue1.dequeue()
            self.Queue2.enqueue(elem)
        
        top = self.Queue1.queue[0]
        self.Queue1.queue = list(self.Queue2.queue)
        self.Queue2.queue = []
        
        return top
        
        

    def top(self) -> int:
        """
        Get the top element.
        """
        
        for i in range(0, self.Queue1.size() - 1):
            elem = self.Queue1.dequeue()
            self.Queue2.enqueue(elem)
        
        top = self.Queue1.queue[0]
        
        # add deleted element to copy queue
        self.Queue2.enqueue(top) 
        self.Queue1.queue = list(self.Queue2.queue)
        self.Queue2.queue = []
        
        return top
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.Queue1.isEmpty()
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(10)
obj.push(1)
obj.push(2)
print(obj.top()) 
print(obj.pop()) 
print(obj.empty())