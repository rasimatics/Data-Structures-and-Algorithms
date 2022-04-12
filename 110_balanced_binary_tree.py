# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        left_height = self.find_height(root.left)
        right_height = self.find_height(root.right)
        
        if not(-1 <= left_height - right_height <= 1):
            return False
        
        return self.isBalanced(root.right) and self.isBalanced(root.left)
        
        
    def find_height(self, root):
        if not root: return -1

        left_height = self.find_height(root.left)
        right_height = self.find_height(root.right)

        return max(left_height, right_height) + 1