# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head 

        while curr:
            temp = curr.next 
            curr.next = prev 
            prev = curr
            curr = temp
        
        return prev 

        

'''
           |   
head = [0, 1, 2, 3]
prev = None 
curr = head (0)

temp = 1
curr.next = None 
prev = 0
curr = 1 


tail becomes head and head becomes tail (we keep swapping positions of nodes)

node 
temp = before head 
prev 
temp = node.val 
node.val = prev 
prev = temp 
'''