# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        #print(node.val)
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next 
            else:
                node.next = list2
                list2 = list2.next 
            node = node.next 
        node.next = list1 or list2 
       
        return dummy.next 
         


'''
             |
list1 = [1,2,4], list2 = [1,3,5]

merged_sorted_list = [1, 1, 2, 3, 4, 5]

compare values from list_1 to list_2 and add smaller values first to 
the merged sorted list


'''

