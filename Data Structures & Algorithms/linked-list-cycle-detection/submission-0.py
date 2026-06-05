# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # use tortoise and hare algorithm to solve this problem 
        slow = head 
        fast = head 

#ensuring that the loop can move the fast pointer two steps ahead without causing a None reference error 
        while fast is not None and fast.next is not None:
            #move slow one step 
            slow = slow.next 
            #move fast two steps 
            fast = fast.next.next 

            if slow == fast:
                return True 
        return False 