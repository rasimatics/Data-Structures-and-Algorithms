# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = ""

        if not root:
            return result
        
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
        result += f"{root.val}"
        
        if left: result += f"({left})"

        if not left and right:
            result += "()"

        if right: result += f"({right})"

        return result
