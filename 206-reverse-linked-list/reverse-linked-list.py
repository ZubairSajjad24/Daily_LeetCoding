# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         temp = head
#         stack = []
        
#         # First pass: Store all values in stack
#         while temp is not None:
#             stack.append(temp.val)  # Push current node's value to stack
#             temp = temp.next
        
#         temp = head  # Reset temp to head for second pass
        
#         # Second pass: Pop values from stack and update nodes
#         while temp is not None:
#             temp.val = stack.pop()  # Replace current value with stack's top
#             temp = temp.next
        
#         return head
        


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head    # Current node we're processing
        prev = None    # Previous node (starts as None)
        
        while temp is not None:
            front = temp.next     # Store next node before we lose it
            temp.next = prev      # Reverse the link: point to previous
            prev = temp           # Move prev pointer forward
            temp = front          # Move current pointer forward
        
        return prev  # prev is now the new head of reversed list