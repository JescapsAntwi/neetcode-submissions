# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #dfs (recursive)
        #the tree could also be considered as a subtree of itself(so this condition leads to true)
        if not subRoot:
            return True 
        if not root:
            return False 
        if self.sameTree(root, subRoot):
            return True 
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        


        #helper function to determine whether the two trees passed to it are identical in both structure and values 
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True 
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))
        return False 