class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
use kadane's algorithm to solve this problem

core idea, for each element nums[i], we either start 
our subarray afresh with it or extend our subarray using nums[i] with the previous sum 

this is greedy because at each step, we choose the 
local best sum hoping it leads to a global best sum 

that is either we start fresh or continue with our streak 

        '''
        current = nums[0]
        maxSum = nums[0]
        
        for num in nums[1:]:
            current = max(num, current + num)
            maxSum = max(maxSum, current)
        return maxSum 