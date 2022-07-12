# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
    
        
        
        
        
#         if head is None:
#             return False
        
#         while head is not None and head.next is not None and head.next.next is not None:
#             if head == head.next:
#                 return True
#             head = head.next
#             head.next = head.next.next
        
#         return False
        