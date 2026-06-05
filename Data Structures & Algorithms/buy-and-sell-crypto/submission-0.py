class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0 
        n = len(prices)
        for i in range(n):
            buy = prices[i]
            for j in range(i+1, n):
                sell = prices[j]
                res = max(res, sell - buy)
        return res 
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

        '''
             #brute force approach 
          
                