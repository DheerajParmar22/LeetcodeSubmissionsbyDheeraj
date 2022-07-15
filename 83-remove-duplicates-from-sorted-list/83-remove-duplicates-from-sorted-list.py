# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        output = head
        while head.next is not None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        
        return output
                
        