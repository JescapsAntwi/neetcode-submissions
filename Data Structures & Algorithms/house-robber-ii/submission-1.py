class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
eliminate all possible sums that include both 
first and last elements

        '''
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums:List[int]) -> int:

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # elif len(nums) == 2:
        #     return max(nums)
        
        # elif len(nums) == 3:
        #     return nums[1]
        

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        #loop
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]
