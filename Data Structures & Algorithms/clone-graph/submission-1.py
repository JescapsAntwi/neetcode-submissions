"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {} #nodes and their new copies (clones)

        #helper dfs function 
        def dfs(node):
            #if we've not created a clone for the node, we add it to our map
            if node in oldToNew: #made a mistake here
                return oldToNew[node]
            copy = Node(node.val) #create a copy of the node (no neighbours right now just the value)
            oldToNew[node] = copy # adding the clone of that node to our map (as value)

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy 
        
        return dfs(node) if node else None
