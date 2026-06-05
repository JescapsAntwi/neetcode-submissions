class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
n directed nodes (1-> n)
times -> list (ui, vi, ti)

ui -> source node 
vi -> target node 
ti -> time taken for signal to travel from source to target node >= 0
k -> the node we will send a signal from 

use djikstra's algorithm (shortest path)

minHeap

path length, Node
0,             1 add this to the heap and then pop this value
1,             3  (pop the value with the min path)
4,             2   (even though this is left, when you pop you realize the node is still 2)
2              4  (this is poppped has shorter path)
3,             2  (this is popped because it is a min heap)

add root node

E = V^2 (every heap operation is worst case Elogv^2)
O(E log v)
        '''
        # create adjacency list for edges: target node, time/ weight to get to that node 
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        
        minHeap = [(0, k)] # path length, node (0 because it takes 0 time to get to the first node)
        visit = set()
        t = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visit) == n else -1
