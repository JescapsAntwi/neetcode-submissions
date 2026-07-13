# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True 
        if not root:
            return False 
        if self.sameTree(root, subRoot):
            return True 
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def sameTree(self, root:Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True 
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))
        return False 

'''
peform dfs starting from root of both trees, check for node value equality at each point
if all passes, return True 

time: O(n)
space: O(n)

For every node in root:

    Is the entire subRoot identical here?

    Yes -> return True
    No  -> try the next node in root
Notice that only root moves. subRoot stays the same because it is the pattern you're trying to find 
throughout the larger tree.
'''