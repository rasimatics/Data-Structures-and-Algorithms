from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        
        
        while head:
            tmp = head.next
            head.next = previous
            previous = head
            head = tmp
            
        
        return previous
            