# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(0)
        cur = res 

        while True:
            minNode = -1 # no minimum node has been found 
            for i in range(len(lists)):
                if not lists[i]:
                    continue 
                if minNode == -1 or lists[minNode].val > lists[i].val:
                    minNode = i
            if minNode == -1:
                break 
            cur.next = lists[minNode]
            lists[minNode] = lists[minNode].next 
            cur = cur.next 
        return res.next 
# O (n * k) n is number of nodes and k is the number of individual lists 


         


'''
Input: lists = [[1,2,4],[1,3,5],[3,6]]

Output: [1,1,2,3,3,4,5,6]

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

minNode = 0 

2 times

[[1, 2, 3], [4, 5, 6]]

'''