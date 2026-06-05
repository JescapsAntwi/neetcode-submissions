"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}
        cur = head 

        #first pass (cloning the linkedlist nodes and adding it to the hashmap)
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy 
            cur = cur.next 
        
        #set the pointers 
        cur = head 
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next 
        
        return oldToCopy[head]

       #map every single old node to the copy of that node we created 
       

       #iterate through the linkedlist once 
       
       

        
        
        
    

        