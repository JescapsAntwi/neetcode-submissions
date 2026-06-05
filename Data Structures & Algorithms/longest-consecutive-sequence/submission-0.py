class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Input: nums = [0,3,2,5,4,6,1,1]
        # store = 7
        # Output: 7
        # brute force approach 
        res = 0
        store = set(nums)

        for num in nums:
            streak, curr = 0, num 
            while curr in store:
                streak += 1
                curr += 1
            
            res = max(res, streak)
        return res
        
