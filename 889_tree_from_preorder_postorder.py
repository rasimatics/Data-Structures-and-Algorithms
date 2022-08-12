# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        if len(preorder) == 0:
            return None
        
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        root = TreeNode(preorder[0])
        count = postorder.index(preorder[1]) + 1
        
        root.left = self.constructFromPrePost(preorder[1 : count + 1], postorder[: count])
        root.right = self.constructFromPrePost(preorder[count+1:], postorder[count:])
        
        return root
        