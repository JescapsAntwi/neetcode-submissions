# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 
        
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, low, high = stack.pop()

            if not (low < node.val < high):
                return False 
            
            #process other nodes and their children 
            if node.left:
                stack.append((node.left, low ,node.val))
            if node.right:
                stack.append((node.right, node.val, high))
            
        return True 



        # if not root:
        #     return False 
        
        # count = 0

        # stack = [(root, 0)]

        # while stack:
        #     node, value = stack.pop()
        #     if node >= value:
        #         count += 1
            
        #     #traverse and append child nodes 
        #     new_val = max(value, node)
        #     if node.left:
        #         stack.append((node.left, new_val))
        #     if node.right:
        #         stack.append((node.right, new_val))
            
        # if count > 0:
        #     return True 
        # else:
        #     return False 


        
    