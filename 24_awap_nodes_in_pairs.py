# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        finalHead = ListNode()
        refToFinalHead = finalHead
        
        while head:
            next = head.next.next if head.next and head.next.next else None
            finalHead.next = self.swapTwoReturnHead(head, head.next)
            finalHead = finalHead.next.next
            head = next
            
        return refToFinalHead.next
    
    def swapTwoReturnHead(self, node1, node2):
        if not node2:
            return node1
        node1.next = node2.next
        node2.next = node1
        return node2

        