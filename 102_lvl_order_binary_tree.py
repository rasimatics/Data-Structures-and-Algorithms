# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        visit = [root]
        res = []
        
        while len(visit) > 0:        
            local_list = []
            current_length = len(visit)
            
            for i in range(current_length):
                node = visit.pop(0)
                if node:
                    local_list.append(node.val)
                    visit.append(node.left)
                    visit.append(node.right)
            
            if local_list:
                res.append(local_list)
        
        return res