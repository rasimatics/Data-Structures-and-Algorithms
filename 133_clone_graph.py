"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
#   DFS
    def cloneGraph(self, node: 'Node') -> 'Node':
        hashmap = {}
        
        def dfs(node):
            if node.val in hashmap:
                return hashmap[node.val]
            
            new_node = Node(node.val)
            hashmap[new_node.val] = new_node

            for i in node.neighbors:
                new_node.neighbors.append(dfs(i))
            return new_node
                    
        return dfs(node) if node else None
    
#   BFS  
    def cloneGraph2(self, node: 'Node') -> 'Node':
        if not node: return None
        
        queue = collections.deque([node])
        created = {node.val: Node(node.val)}
        
        while queue:
            item = queue.popleft()
            current = created[item.val]
            
            for i in item.neighbors:
                if i.val not in created:
                    created[i.val] = Node(i.val)
                    queue.append(i)
                current.neighbors.append(created[i.val])
                        
        return created[node.val]
            