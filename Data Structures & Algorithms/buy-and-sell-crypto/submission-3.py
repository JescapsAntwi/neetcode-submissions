class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pos_diff = []
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] >= 0:
                    pos_diff.append(prices[j] - prices[i])
        if len(pos_diff) >= 1:
            return max(pos_diff)
        else:
            return 0

'''
max = 0 
                   |
                     |
prices = [10,1,5,6,7,1]
max (positive differences) 
max([4, 5, 6, 0, 1, 2, 1]) = 6 

                 |
                   |
prices = [10,8,7,5,2]
max([])
time: O(n2)
space: O(n)
'''