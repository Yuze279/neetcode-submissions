# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        current = head #of the lsit

        #swapping the current and previous
        #edge case just reaturn head or 
        # return previous?

        while current: #is a value that's not none 
            temp = current.next
            current.next = prev
            prev = current
            current = temp 

    
        return prev
