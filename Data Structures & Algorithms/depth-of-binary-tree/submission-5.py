# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #empty tree 
        if not root:
            return 0
        #bfs 
        q = deque() #
        if root:
            q.append(root) 
        level = 0 # 3
        while q:
            for i in range(len(q)):
                node = q.popleft() # 4 
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        
        return level 




        
        
        

'''
stack = [root]
        while stack:
            depth = 0
            node = stack.pop()
            while node.left or node.right:
                depth += 1
                stack.append(node.left)
                stack.append(node.right)
        
        return depth 

#iterative dfs 
        stack = [(root, 1)] # to keep track of each node and its depth
        max_depth = 0 
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)

            if node.right:
                stack.append((node.right, depth + 1))
            
            if node.left:
                stack.append((node.left, depth + 1))
        
        return max_depth

#recursive dfs 
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        return max(leftDepth, rightDepth) + 1
'''

        