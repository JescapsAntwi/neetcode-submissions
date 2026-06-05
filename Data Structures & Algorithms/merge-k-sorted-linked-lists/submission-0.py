# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for lst in lists: # O(n)
            while lst:
                nodes.append(lst.val)
                lst = lst.next 
        
        nodes.sort() # O(logn) 
        dummy = ListNode(0)
        cur = dummy 
        for node in nodes:
            cur.next = ListNode(node)
            cur = cur.next
        return dummy.next 


'''
minNode = 0 

2 times

[[1, 2, 3], [4, 5, 6]]

'''