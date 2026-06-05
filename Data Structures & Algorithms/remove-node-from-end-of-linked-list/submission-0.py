# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head 

        #move right pointer n times 
        while n > 0:
            right = right.next 
            n -= 1
        
        #shift both left and right pointers 
        while right:
            left = left.next 
            right = right.next 
        
        #delete nth node and return head of list 
        left.next = left.next.next 
        return dummy.next 
        
'''
possible solution: reverse linkedList and traverse from end (now head)
most linkedList problems use two pointers 
algorithm: start left node from dummy node (this helps in deletion of the nth node)
right pointer starts from head 
shift right pointer by n times 
then shift both left and right pointers forward until right pointer is null
when right reaches null, the left pointer will be at the node before the nth node 
so we connect the nth - 1 node to nth + 1 node 
then return dummy.next (head of linked list)
'''