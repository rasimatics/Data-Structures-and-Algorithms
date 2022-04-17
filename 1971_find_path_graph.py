class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        nbrs = {i: [] for i  in range(n)}
        
        for i, j in edges:
            nbrs[i].append(j)
            nbrs[j].append(i)
        
        queue = [source]
        visited = []
        
        while queue:
            node = queue.pop(0)
            visited.append(node)
            
            if node == destination:
                return True
            
            for i in nbrs[node]:
                if i not in visited:
                    queue.append(i)
                    
        return False