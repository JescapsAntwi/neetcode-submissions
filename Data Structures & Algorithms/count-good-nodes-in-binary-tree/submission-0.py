# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0 

        stack = [(root, root.val)]

        count = 0

        while stack:
            node, max_val = stack.pop()
            if node.val >= max_val:
                count += 1
            
            new_max = max(max_val, node.val)
            if node.left:
                stack.append((node.left, new_max))
            if node.right:
                stack.append((node.right, new_max))
        
        return count 




        # count = 1 
        # while stack:
        #     node = stack.pop()

        #     if node.left or node.left.val > root.val:
        #         node = node.left 
        #         count += 1
        #     if node.right or node.right.val > root.val:
        #         node = node.right 
        #         count += 1
        
        # return count 

'''
root is always a good node: there's always at least one good node in the binary tree
'''