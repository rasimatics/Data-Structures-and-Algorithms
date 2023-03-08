# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        
        if not postorder:
            return None

        val = postorder[-1]
        root = TreeNode(val=val)

        index = inorder.index(val)
        left_ino = inorder[:index]
        right_ino = inorder[index+1:]

        index = len(left_ino)
        left_post = postorder[:index]
        right_post = postorder[index:len(postorder)-1]

        root.left = self.buildTree(left_ino, left_post)
        root.right = self.buildTree(right_ino, right_post)

        return root
    



