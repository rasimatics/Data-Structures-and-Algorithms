from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    self.bfs(r, c, visited, rows, cols, grid)
                    islands += 1

        return islands

    def bfs(self, row, col, visited, rows, cols, grid):
        queue = deque()
        queue.append((row,col))

        while queue:
            r, c = queue.pop()
            visited.add((r, c))
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            
            for d in directions:
                next_r = r + d[0]
                next_c = c + d[1]
                
                if -1 < next_r < rows and -1 < next_c < cols and grid[next_r][next_c] == "1" and (next_r, next_c) not in visited:
                    queue.append((next_r, next_c))



