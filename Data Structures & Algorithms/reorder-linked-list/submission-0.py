# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #fast and slow pointers 
        slow, fast = head, head.next 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        
        #reversal logic + splitting of list 
        second = slow.next 
        prev = slow.next = None #head of the second list to be reversed 
        while second:
            temp = second.next 
            second.next = prev 
            prev = second 
            second = temp 
        
        #merge logic 
        first, second = head, prev 
        while second:
            temp1, temp2 = first.next, second.next 
            first.next = second 
            second.next = temp1 
            first, second = temp1, temp2 

'''
2, 4, 8, 6
[2, 8,  8, 4]
    |      |

4, 6 

2 -> 8 -> 8 -> 4
     |         |
   4    6 


2 -> 8 -> 4 -> 6

[2, 8, 4, 6]

[2, 4, 6, 8, 10]
       |    
       
               |   

               2, 10, 4, 6, 8  
second = 8
prev = 

tmp = 10 
prev = 8


f= 4, s = 6
2 -> 8 -> 6
10 -> 4

2 -> 10 -> 4 -> 8 -> 6
[2, 10, 4, 8, 6]



keep head 
swap tail with node after head 
update tail node 
process continues 

take the entire list into array 
take the second portion of the list, reverse it and take the first portion 
and merge them together. 

steps:
1. find the middle of the list 
when fast reaches the end, slow will be at the midpoint 

2. reverse the second half 

3. merge the two lists alternately 
'''