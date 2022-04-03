# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
#       seperate left and right
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        right = slow.next
        slow.next = None
        
#       reverse right 
        tmp = right
        prev = None
        while tmp:
            tmp_next = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = tmp_next
            
#       combine
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
            
            
        
        
        
        
        