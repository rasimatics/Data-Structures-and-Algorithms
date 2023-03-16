# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
      """
          Space  O(1)
          Time   O(n)
      """
        fast, slow = head, head
        prev = None
        temp = None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = slow
        slow = slow.next
        prev.next = None

        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        slow = prev
        while slow:
            if slow.val != head.val: return False
            
            slow = slow.next
            head = head.next
        
        return True

    
    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
      """
          Space  O(n)
          Time   O(n)
      """
        result = ""
        
        while head:
            result += f"{head.val}"
            head = head.next

        return result == result[::-1]    
