# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None 
        
        queue = deque([root]) #initializing a queue with the root node 

        #while the queue is not empty 
        while queue:
            node = queue.popleft() #dequeue a node from the front 
            node.left, node.right = node.right, node.left 

            #enqueue the children of the dequeued node 
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root 