class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #i, j = 0, 1
        for i in range(len(nums)): #  no zero
            for j in range(i + 1, len(nums)): # i + 1
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
                #else:
                    #i += 1
                    #j += 1 []
                


'''
 |       -> i (0)
   |     -> j (1)
[3,4,5,6], target = 7

nums[0] + nums[1] = 3 + 4 = 7

[0, 1]

|
     |
[4,5,6], target = 10
nums[0] + nums[2] = 10 = 10 

time: O(n2)
space: O(1)
'''