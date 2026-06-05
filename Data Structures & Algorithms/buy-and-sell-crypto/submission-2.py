class Solution:
    def maxProfit(self, prices: List[int]) -> int:


     #optimal approach using dynamic programming 
        maxP = 0 
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP
        '''
if not prices:
            return 0
        n = len(prices)
        res = []
        for i in range(n):
            for j in range(i+1, n):
                profit = prices[j] - prices[i]
                res.append(profit)
        sort_res = sorted(res)
        for num in sort_res:
            if num > 0:
                return max(num, sort_res)
            else:
                return 0

                maxP = 10
                minBuy = 10
                                      \        l       r
                Input: prices = [10,1,5,6,7,1]

                Output: 6


        '''
             
          
                