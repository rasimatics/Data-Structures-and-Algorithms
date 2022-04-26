# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        prev = None
        mid = None
        last = None
        
        def dfs(root):
            nonlocal prev, mid, last
            if not root: return
            
#           Inorder traversal
            dfs(root.left)
            if prev and prev.val > root.val:
                if mid == None:
                    mid = prev
                    last = root
                else:
                    last = root
            prev = root
            dfs(root.right)
            
        dfs(root)
        
        tmp = mid.val
        mid.val = last.val
        last.val = tmp
        
               
    def recoverTree2(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = []
        def dfs(root):
            if not root: return
            
            dfs(root.left)
            arr.append(root)
            dfs(root.right)
            
        dfs(root)
        
        srt = sorted(i.val for i in arr)
        
        for i in range(len(srt)):
            arr[i].val = srt[i]
            
        
        
        