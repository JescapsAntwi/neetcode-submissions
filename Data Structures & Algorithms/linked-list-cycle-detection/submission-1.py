# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head 
        fast = head 

        while fast is not None and fast.next is not None:
            slow = slow.next 
            fast = fast.next.next 

            if slow == fast:
                return True 
        return False 


'''
use fast and slow pointers to detect cycles in the linked lists

slow = head 
fast = head 

slow = one step = slow.next  = 2 = 4 
fast = two steps = fast.next.next = 3 = 4
        |
        |
head = [1,2,3,4], index = 1

           |
           |    
1 - 2 - 3- 4

true 
          |
        |
head = [1,2], index = -1

time: O(n)
space: O(1)
'''