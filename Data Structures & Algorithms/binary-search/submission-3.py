class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


'''
         |
                   |
nums = [-1,0,2,4,6,8], target = 4
mid = (l + r) // 2 = 3

               | 
             |
nums = [-1,0,2,4,6,8], target = 3
mid = 3
return -1

mid < target: l = mid + 1
mid > target: r = mid - 1

outside: return -1 
time: O(logn)
space: O(1)

'''