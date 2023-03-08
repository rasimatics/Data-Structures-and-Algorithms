from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = set()

        def bfs(row, col):            
            q = deque()
            q.append((row, col))

            while q:
                r, c = q.pop()
                visited.add((r,c))
                
                directions = [[0,1],[0,-1],[1,0],[-1,0]]

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    
                    if -1 < nr < rows and -1 < nc < cols and (nr, nc) not in visited and board[nr][nc] == "O":
                        q.append((nr, nc))

        
        for i in range(rows):
            if board[i][0] == "O" and (i, 0) not in visited:
                bfs(i, 0)
            
            if board[i][cols-1] == "O" and (i, cols-1) not in visited:
                bfs(i, cols - 1)
                

        for j in range(cols):
            if board[0][j] == "O" and (0, j) not in visited: 
                bfs(0, j)

            if board[rows-1][j] == "O" and (rows-1, j) not in visited:
                bfs(rows - 1, j)
                

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"

        



    def solve2(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = set()
        non_problematic = []

        def make_x(row, col):
            visited = set()
            q = deque()
            q.append((row, col))

            while q:
                r, c = q.pop()
                visited.add((r,c))
                board[r][c] = "X"

                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    
                    if -1 < nr < rows and -1 < nc < cols and (nr, nc) not in visited and board[nr][nc] == "O":
                        q.append((nr, nc))




        def bfs(row, col):            
            q = deque()
            q.append((row, col))

            while q:
                r, c = q.pop()
                visited.add((r,c))

                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    non_problematic.append((r, c))
                
                directions = [[0,1],[0,-1],[1,0],[-1,0]]

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    
                    if -1 < nr < rows and -1 < nc < cols and (nr, nc) not in visited and board[nr][nc] == "O":
                        q.append((nr, nc))


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visited:
                    before_len = len(non_problematic)
                    bfs(r,c)
                    after_len = len(non_problematic)

                    if before_len == after_len:
                        make_x(r, c)
