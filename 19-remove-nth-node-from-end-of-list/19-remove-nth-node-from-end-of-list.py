# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head == None:
            return None
        
        dummy_head = ListNode(0,head)
        left = dummy_head
        right = head
        
        while n>0:
            right = right.next
            n -= 1
            
        while right:
            right = right.next
            left = left.next
            
        left.next = left.next.next
        
        return dummy_head.next
        
        
        
        
        
        
        
        
        
        
        
#         prev_end_node = dummy_head = ListNode(next=head)
#         curr_node = head
#         index = 1
#         while index < n:
#             curr_node = curr_node.next
#             index += 1
            
#         while curr_node.next:
#             curr_node = curr_node.next
#             prev_end_node = prev_end_node.next
#         else:
#             prev_end_node.next = prev_end_node.next.next
        
#         return dummy_head.next
        