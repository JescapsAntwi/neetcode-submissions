class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
koko can only eat at most one pile of banana in a given hour
len(p) <= h 

k = bananas per hour eating rate

each hour - eat k bananas from that pile

[1, 4, 3, 2], h = 9

k = 2
1 + 2 + 2 + 1 = 6 hours 

Search Space: k must be between 1 (slowest) and max(piles) (fastest possible).
Monotonic Property:

If k is too small → total time > h (too slow).
If k is too large → total time ≤ h (fast enough).
Optimal k: The smallest k where total time ≤ h.

For every pile, calculate ceil(pile / k).
Sum all these times to get totalTime.
Check if totalTime ≤ h:

If yes, k is a candidate (try to find a smaller k).
If no, k is too slow (try a larger k).
        '''
        l, r = 1, max(piles) #defining the search range
        res = r # worst case (fastest possible k)

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile) / k)
            #k is a candidate so we now have to find the minimum k 
            if totalTime <= h: # k is large (more bananas per hour)
                res = k
                r = k - 1 # search left 
            else:
                l = k + 1 # k is small (less piles of bananas per hour)
        return res 



