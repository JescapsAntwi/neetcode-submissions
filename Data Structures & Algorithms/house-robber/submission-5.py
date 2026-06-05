class Solution:
    def rob(self, nums: List[int]) -> int:
        
        '''
0-indexed based array of money
straight line: second house is neighbour of first house and third house

cannot rob two adjacent houses 

 total = 0

        for i in range(len(nums)):
            if i % 2 != 0:
                continue
            elif i % 2 == 0:
                total += nums[i]
        return total
        '''
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        return dp[-1]
       