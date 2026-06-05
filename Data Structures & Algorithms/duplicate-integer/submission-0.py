class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
initialize a set to contain unique elements 
loop through array and add elements to set 
check if length of array is not equal to set
return true if different, else false 
        '''
        unique_elements = set()
        for num in nums:
            unique_elements.add(num)
        return len(unique_elements) != len(nums)