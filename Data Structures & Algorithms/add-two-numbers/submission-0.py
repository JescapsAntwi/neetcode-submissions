# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        #create dummy node to deal with inserting into linkedlist
        dummy = ListNode()
        cur = dummy # points at the position that we will be inserting a new node (digit)
        
        carry = 0 # carry value that we will have to maintain 
        while l1 or l2 or carry: # both lists could be empty but there will be a carry so we have to consider that edge case 


            v1 = l1.val if l1 else 0 #get value from first list if l1 isn't null/ empty 
            v2 = l2.val if l2 else 0 # same for l2 

            # new digit 
            val = v1 + v2 + carry
            # getting the carry out of double digit values 
            carry = val // 10 
            val = val % 10 # getting the ones place value
            cur.next = ListNode(val) # insert new digit into linkedlist 

                #update pointers 
            cur = cur.next 
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None 

        return dummy.next 
        
            


