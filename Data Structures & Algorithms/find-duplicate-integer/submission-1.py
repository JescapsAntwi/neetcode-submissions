class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        set = {1, 2, 3}
        seen_set = set()
        for num in nums:
            if num not in seen_set:
                seen_set.add(num)
            else:
                return num 
        
        linked list cycle problem 
        use fast and slow pointers (it helps in determining cycles in linkedlists)

        2 x slow = fast 
        '''
        slow, fast = 0, 0 # both start from 0 because we know 0 is not part of the cycle 
        while True: # we keep looping until slow and fast intersect 
            slow = nums[slow]
            fast = nums[nums[fast]] # we are advancing fast twice 
            if slow == fast:
                break 
        
        slow2 = 0
        while True:
            slow =nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break 
        return slow 


        
        
        