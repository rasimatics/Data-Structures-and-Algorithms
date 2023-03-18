class Trie:

    def __init__(self):
        self.childrens = {}
        self.is_end = False
        

    def insert(self, word: str) -> None:
        node = self
        
        for i in word:
            if i in node.childrens:
                node = node.childrens[i]
            else:
                new_node = Trie()
                node.childrens[i] = new_node
                node = node.childrens[i]
                
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self

        for i in word:
            if i not in node.childrens:
                return False
            
            node = node.childrens[i]

        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self

        for i in prefix:
            if i not in node.childrens:
                return False
            
            node = node.childrens[i]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
