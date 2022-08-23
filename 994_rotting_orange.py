class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minuteTracker = 0
        fresh = 0
        queue = []
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append([i,j,0])
                elif grid[i][j] == 1:
                    fresh += 1
        
        while queue:
            i, j, minute = queue.pop(0)
            minuteTracker = max(minuteTracker, minute)
            minute += 1
            
            if i + 1 < len(grid) and grid[i+1][j] == 1:
                queue.append([i+1,j,minute])
                grid[i+1][j] = 2
                fresh -= 1
            
            if i - 1 >= 0 and grid[i - 1][j] == 1:
                queue.append([i-1,j, minute])
                grid[i - 1][j] = 2
                fresh -= 1
                
            if j + 1 < len(grid[i]) and grid[i][j+1] == 1:
                queue.append([i,j+1,minute])
                grid[i][j+1] = 2
                fresh -= 1
                
            if j - 1 >= 0 and grid[i][j-1] == 1:
                queue.append([i,j-1,minute])
                grid[i][j-1] = 2
                fresh -= 1
                
        return minuteTracker if fresh == 0 else -1
        
        
    
                    