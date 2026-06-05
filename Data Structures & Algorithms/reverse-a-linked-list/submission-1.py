# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #use in place reversal of linkedlist to solve this problem. (no extra space)
        prev = None 
        curr = head 

        while curr is not None:
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp 
        return prev 


# 0 -> 1 -> 2 -> 3
# 0(p) -> 1(c) -> 2 -> 3
#   0    -> 1(p) -> 2(c) -> 3
#   0     -> 1 -> 2(p) -> 3(c)
# 0 -> 1 -> 2 -> 3(p) -> c(None)