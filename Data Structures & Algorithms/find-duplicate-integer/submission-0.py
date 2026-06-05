class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        set = {1, 2, 3}
        '''
        seen_set = set()
        for num in nums:
            if num not in seen_set:
                seen_set.add(num)
            else:
                return num 
        
        