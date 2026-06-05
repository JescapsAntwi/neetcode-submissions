class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1): #it is len(cost) -3 because we look two steps ahead (i+1 and i+2) so we must stop before we go out of bounds
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])

        


        '''
        Here's how i understand this problem
        we are given a staircase and we are asked to find the cost of the minimum number of steps taken 
        to reach the top at any point (step) in the staircase

        approach 
        use dp (space optimized) and start from the last step (makes sense since at the last step, we take only 
        zero steps to reach the top, so it is the cost at that step)

        same for the last but one step, it takes just 1 step to get to the top. we can start at the 0 or 1 step per the requirement of the question. 

        building on this, we loop backwards from the last step, decrementing our indices and for each index, we update the cost at that index in our cost array 
    the minimum of the cost at the next index and the second next index. 

    when done looping, pick the smallest of the first and second costs and return it. 

because we can start at either the 0 or 1 step to reach to the top

        '''