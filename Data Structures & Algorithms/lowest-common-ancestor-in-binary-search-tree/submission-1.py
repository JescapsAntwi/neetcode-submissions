# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #base case 
        if not root or not p or not q:
            return None 
        
        if (min(q.val, p.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        elif (max(q.val, p.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root 

        '''
the root is always going to be a common ancestor for all the nodes in the tree
so we always start at the root. 

- if p and q are both less than root, traverse left subtree
- if less, traverse right subtree 
- if one is in the right subtree and the other in the left subtree, the 
root node is the LCA 
- if we traverse and reach the node itself, it is the LCA

root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4

     5
    / \
    3  8 
    /\  /\
    1 4 7 9 
    \ 
     2 
        '''