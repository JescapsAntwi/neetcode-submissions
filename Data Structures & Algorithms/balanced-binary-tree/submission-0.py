# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
                 #an empty tree is balanced so we return true 
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            #for a tree to be balanced, jevery node and subtree should be balanced 
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            #returning the boolean and height of the subtree
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0] #we are only interested in the boolean 
