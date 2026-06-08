class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers_seen = set()
        #numbers_seen.add(nums)

        for num in nums:
            if num in numbers_seen:
                return True 
            numbers_seen.add(num)
        return False 

            #numbers_seen.add(num)
            
                #return True
        #return False 
            

'''
[1, 2, 3, 3]
[1, 2, 3, 4]
set = {1, 2, 3, 4}
'''