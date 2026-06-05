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

brute force: return min(nums)

The algorithm always moves toward the unsorted half, where the minimum must reside. It updates res whenever it finds a smaller value, ensuring the correct minimum is returned.

Summary

The "pivot" is where the rotation happens, but the algorithm doesn't need to find it explicitly.
The minimum is found by always moving toward the unsorted half and keeping track of the smallest value seen so far.
        '''
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break 
            
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        return res 
        
        