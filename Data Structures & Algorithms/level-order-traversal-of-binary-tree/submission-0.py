# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        queue.append(root)

        result = []

        while queue:
            queue_length = len(queue)
            level = []
            # dequeue all nodes at the same level and enqueue their children 
            for i in range(queue_length):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
                # if node:
                    
        #             queue.append(node.left)
        #             queue.append(node.right)
        #         if level:
        #             result.append(level)
        # return res 
        #     node = queue.popleft() # 1 
        #     result.append([node.val]) # [[1]]
        #     if node.left:
        #         node = node.left 
        #     elif node.right:
        #         node = node.right 
        
        # return result
            

        '''
perform level order traversal (bfs) by processing nodes level by level 
the root node is the first sublist 
dequeue all the nodes at the same level and add their values to a list 
then enqueue their children and add their children to the queue (left first, then right)
add this list to the bigger list and return it
        '''