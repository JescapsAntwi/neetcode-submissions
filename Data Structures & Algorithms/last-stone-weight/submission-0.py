class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #we used a min-heap to simulate max-heap behaviour 
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1: # [-1, -2]
            first = heapq.heappop(stones)#first largest number 
            second = heapq.heappop(stones) #second largest number 
            if second > first:
                heapq.heappush(stones, first - second)
        
        #edge case if our heap is empty. we return 0 if there aren't any stones remaining  
        stones.append(0)
        return abs(stones[0]) # weight of the last remaining stone 