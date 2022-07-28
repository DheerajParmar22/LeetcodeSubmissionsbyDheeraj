# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head and not head.next or not head:
            return head
        
        slow = fast = head
        while fast and fast.next:
            slow.val, slow.next.val = slow.next.val, slow.val
            fast = fast.next.next
            slow = fast
        
        return head
        