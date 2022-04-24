class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}
        
        for i, j in prerequisites:
            adjList[i].append(j)
        
        visited = set()
        
        def dfs(node):
            if node in visited:
                return False
            
            if adjList[node] == []:
                return True
            
            visited.add(node)
            for i in adjList[node]:
                if not dfs(i): return False
            visited.remove(node)
            adjList[node] = []
            return True
        
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True
            
        
            
            
        
        
        
        
        
        
        
        
            