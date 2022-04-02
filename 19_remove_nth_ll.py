# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dump = ListNode()
        tail = dump
        tmp = head
        
#       Determine length of LL
        length = 0
        while tmp:
            tmp = tmp.next
            length += 1
            
#       skip nth  node
        i = 0
        while head:
            if length - i != n:
                tail.next = head
                tail = head
            
            head = head.next
            i += 1
            
        tail.next = None
        return dump.next