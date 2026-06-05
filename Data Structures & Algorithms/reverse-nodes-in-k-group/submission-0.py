# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head 
        group = 0 
        while cur and group < k:
            cur = cur.next 
            group += 1
        
        if group == k:
            cur = self.reverseKGroup(cur, k) # pointing cur to the next k reversed group 
            while group > 0:
                tmp = head.next # temporarily store the next node 
                head.next = cur # link the current node to the reversed next group 
                cur = head 
                head = tmp 
                group -= 1
            head = cur 
        return head 

        

        '''
reverse the current k nodes and link to the next reversed k nodes and do this recursively 
until all the nodes in the list have been processed 


        '''