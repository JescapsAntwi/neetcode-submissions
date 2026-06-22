# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # dfs 
        if not root:
            return None 
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root  
        
       
  

'''
level order traversal (modified)
visit all nodes in the right subtree of the root node before visiting 
the left subtree (on the same level before moving down to another level)
do this at each level

 result = []
    
    def levelOrder(node):
        if node: 
            result.append(node.val)
            levelOrder(node.right)
            levelOrder(node.left)
    levelOrder(root)
    return result
'''