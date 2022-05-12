# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def construct(preorder, inorder):
            if len(preorder) == 1:
                return TreeNode(val = preorder[0])
            if len(preorder) == 0 or len(inorder) == 0:
                return None
            
            root = TreeNode(val = preorder[0])
            mid = inorder.index(root.val)
            left_ino = inorder[0 : mid]
            left_pre = preorder[1 : mid + 1]
            root.left = construct(left_pre, left_ino)
            
            right_ino = inorder[mid + 1:]
            right_pre = preorder[mid + 1:]
            root.right = construct(right_pre, right_ino)
            
            return root
        return construct(preorder, inorder)
        
        