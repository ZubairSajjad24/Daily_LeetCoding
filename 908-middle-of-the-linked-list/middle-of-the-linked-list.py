# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         n = 0
#         temp = head
#         # First pass: count the total number of nodes
#         while temp:
#             n += 1                          # increment counter
#             temp = temp.next                # move to next node
        
#         temp = head
#         # Second pass: move to the middle position
#         for i in range(n // 2):
#             temp = temp.next                # move forward n//2 steps
#         return temp                         # return the middle node


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head                         # slow pointer starts at head
        fast = head                         # fast pointer starts at head
        
        # Move until fast pointer reaches the end
        while fast and fast.next:
            slow = slow.next                # slow moves 1 step
            fast = fast.next.next           # fast moves 2 steps
        
        return slow                         # slow is now at the middle






        