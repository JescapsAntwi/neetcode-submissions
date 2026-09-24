class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_values = set()

        for num in nums:
            if num in unique_values:
                return True 
            unique_values.add(num)
        return False 

'''
nums = [1, 2, 3, 3]
set = {1, 2, 3}

'''