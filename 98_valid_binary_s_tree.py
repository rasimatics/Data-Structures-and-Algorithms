# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, left, right):
            if not node: return True
            if not (left < node.val < right): return False
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        return valid(root, float('-inf'), float('+inf'))
    
    
    
    
    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        if not root: return root
        arr = []
        
        def dfs(root):
            if not root: return None
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right) 
            
        def check_arr(arr):
            for i in range(1, len(arr)):
                if arr[i] <= arr[i - 1]:
                    return False
            return True
                
        dfs(root)
        return check_arr(arr)
        