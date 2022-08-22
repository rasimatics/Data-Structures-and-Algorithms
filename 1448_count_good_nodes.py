# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return
        
        return 1 + self.checkNodes(root.left, root.val) + self.checkNodes(root.right, root.val)
    
    def checkNodes(self, node, max_value):
        if not node:
            return 0
        
        _max = max_value
        _count = 0
        
        if node.val >= max_value:
            _max = node.val
            _count = 1
        
        return _count + self.checkNodes(node.left, _max) + self.checkNodes(node.right, _max)
        

            
        
        
            
                
                    