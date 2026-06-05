# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root 

        while curr:
            #both p and q are greater than root node 
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            #both p and q are lesser than root node 
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left 
            #split (one is lesser and one is greater)
            else:
                return curr 
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