class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, max_profit = 0, 1, 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)
            else:
                left = right 
            right += 1
        return max_profit
        
'''
max_profit = 6
            |
            |
[10,1,5,6,7,1]
4, 5, 6

time: O(n)
space: O(1)
'''