"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
        
        1 1 0 0 
        0 0 1 1
        1 1 0 0
        0 0 1 1
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        root = Node(0, 0, None, None, None, None)

        n = len(grid)
        
        if n == 1:
            root.isLeaf = 1
            root.val = grid[0][0]
            return root
        
        elif n == 2:
            if grid[0][0] == grid[1][1] == grid[0][1] == grid[1][0]:
                root.val = grid[0][0]
                root.isLeaf = 1

            else:
                root.val = 1
                root.isLeaf = 0
                root.topLeft = Node(grid[0][0], 1, None, None, None, None)
                root.topRight = Node(grid[0][1], 1, None, None, None, None)
                root.bottomLeft = Node(grid[1][0], 1, None, None, None, None)
                root.bottomRight = Node(grid[1][1], 1, None, None, None, None)

            return root
        
        elif n > 2:
            root.topLeft = self.construct([i[:n//2] for i in grid[:n//2]])
            root.topRight = self.construct([i[n//2:] for i in grid[:n//2]])
            root.bottomLeft = self.construct([i[:n//2] for i in grid[n//2:]])
            root.bottomRight = self.construct([i[n//2:] for i in grid[n//2:]])
            
            if root.topLeft.val == root.topRight.val == root.bottomLeft.val == root.bottomRight.val and root.topLeft.isLeaf == root.topRight.isLeaf == root.bottomLeft.isLeaf == root.bottomRight.isLeaf == 1:
                root.isLeaf = 1
                root.val = root.topLeft.val
                root.topLeft = None
                root.topRight = None
                root.bottomLeft = None
                root.bottomRight = None
            else:
                root.isLeaf = 0
                root.val = 1
                         
            return root
            
            