class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        return str(self.value)


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.dict = {}
        self.head = Node('head', 'start')
        self.tail = Node('tail', 'finish')
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_before(self, new_node) -> None:
        head = self.head.next
        new_node.prev = head.prev
        new_node.next = head
        head.prev = new_node
        self.head.next = new_node

    def remove_node(self, node) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key in self.dict.keys():
            node = self.dict[key]
            value = node.value
            self.remove_node(node)
            self.insert_before(node)
            return value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.dict.keys():
            node = self.dict[key]
            node.value = value
            self.remove_node(node)
            self.insert_before(node)
        else:
            if len(self.dict) >= self.capacity:
                node = self.tail.prev
                del self.dict[node.key]
                self.remove_node(node)
            
            new_node = Node(key, value)
            self.insert_before(new_node)
            self.dict[key] = new_node


            

lRUCache =  LRUCache(2)
lRUCache.put(2, 1)  
lRUCache.put(1, 1) 
lRUCache.put(2, 3) 
lRUCache.put(4, 1) 
print(lRUCache.dict)
print(lRUCache.get(1)) 
print(lRUCache.get(2))  


