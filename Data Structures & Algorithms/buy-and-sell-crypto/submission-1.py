class Solution:
    def maxProfit(self, prices: List[int]) -> int:


     #optimal approach using two pointers
        l, r = 0, 1 
        maxP = 0 
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r 
            r += 1
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
                maxP = 6
                l, r = 0, 6
                                            l       r
                Input: prices = [10,1,5,6,7,1]

                Output: 6


        '''
             
          
                