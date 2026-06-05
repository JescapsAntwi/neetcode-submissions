class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Input: nums = [0,3,2,5,4,6,1,1]
        # store = 7
        # Output: 7
        # optimal approach using a hashset 
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest 
