class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
brute force: linear search 
 for i in range(len(nums)):
            if nums[i] == target:
                return i 
        return -1 

optimal approach with binary search 
        '''
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid 
            
            #check if left half is sorted 
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]: 
                    #search right half 
                    l = mid + 1
                else:
                    # search left half 
                    r = mid - 1
            
            #check if right half is sorted 
            else:
                if target < nums[mid] or target > nums[r]:
                    #search left half 
                    r = mid - 1
                else:
                    l = mid + 1
        return -1 




        


       