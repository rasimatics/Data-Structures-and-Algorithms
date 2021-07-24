class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size or self.head == None:
            return -1
        
        c_head = self.head
        
        for _ in range(index):
            c_head = c_head.next
        
     
        return c_head.value
        
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        c_head = self.head

        if not c_head:
            self.head = Node(val)
        
        else:
            while c_head.next:
                c_head = c_head.next
    
            c_head.next = Node(val)
        
        self.size += 1

        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """

        if index > self.size:
            return


        if index == 0:
            self.addAtHead(val)
        
        elif index == self.size:
            self.addAtTail(val)
        else:
            c_head = self.head

            for _ in range(index-1):
                c_head = c_head.next
            
            new_node = Node(val)
            new_node.next = c_head.next
            c_head.next = new_node
            self.size += 1




    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """

        if index < 0 or index >= self.size or self.head == None:
            return

        if index == 0:
            self.head = self.head.next
        else:
            c_head = self.head

            for _ in range(index-1):
                c_head = c_head.next

            c_head.next = c_head.next.next
            
        self.size -= 1
