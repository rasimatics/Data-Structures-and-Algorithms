# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode()
        copy_l = left
        
        right = ListNode()
        copy_r = right
        
        while head:
            if head.val < x:
                copy_l.next = head
                copy_l = head
            else:
                copy_r.next = head
                copy_r = head
            head = head.next
        
        copy_r.next = None
        copy_l.next = right.next
        
        return left.next
        
        
