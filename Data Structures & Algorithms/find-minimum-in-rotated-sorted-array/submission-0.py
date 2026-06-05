class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
set min as first element 

check if nums[l] < nums[r]
update res 
break 

else 
get mid 
if nums[mid] >= nums[l]
l = m + 1
else:
    r = mid - 1

original_array = [1, 2, 3, 4, 5]
rotated_array = [4, 5, 1, 2, 3]   #2 times
        '''
        return min(nums)
        