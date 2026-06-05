class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #nums = [1, 2, 3, 4], target = 5
        '''
approach: use two pointers technique 
first pointer at start 
second pointer at end of array 
traverse array
while left < right:
    current_sum = arr[left] + [right]
    check if current_sum is equal to target
    if equal return [left, right]
    else:
        adjust pointers based on relative size to target 
    move outside loop and return [updated pointers]  

time and space complexities: O(n), we go through the array once and O(n) space 
occupied by current_sum array 

  left = 0
        right = len(nums) - 1 # 1

        while left < right:
            current_sum = nums[left] + nums[right] #-4
            if current_sum == target:
                return [left, right]
            if current_sum < target:     #[-1, -2, -3, -4, -5] -8
                left += 1
            elif current_sum > target:
                right -= 1 
        return [left, right]
        '''
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n 
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return []
      
