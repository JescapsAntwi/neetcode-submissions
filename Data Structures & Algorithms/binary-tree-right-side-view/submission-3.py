# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = [(root, 0)] # node, depth 
        #stack.append(root)

        result = []

        while stack:
            node, depth = stack.pop()
            if depth == len(result): # if this is the first node encountered at this depth, add its value to the result list 
                result.append(node.val)

            #process left child first due to stack's LIFO 
            if node.left:
                stack.append((node.left, depth + 1))
            
            if node.right:
                stack.append((node.right, depth + 1))
        
        return result 



            #result.append(node.val)

        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         continue 

        # return result 
            



'''
use dfs to traverse tree
start from root, if left node is not null, skip it
if right node is not null, add its node to the result list 
repeat for all nodes and return list 

'''
        