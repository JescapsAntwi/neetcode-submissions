# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #recursive dfs 
        if not root:
            return None 
        root.left, root.right = root.right, root.left 

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root 
        '''
root, right, left (for each node) -- modified pre order traversal 

 result = []
def modified_pre_order(node):

    if node:
        result.append(node.val)
        modified_pre_order(node.right)
        modified_pre_order(node.left)
    
modified_pre_order(root)
return result
      
Input: root = [1,2,3,4,5,6,7]

Output: [1,3,2,7,6,5,4]


stack = []

node = 7
l= 7
r = 6
        '''
        
