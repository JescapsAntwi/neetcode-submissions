class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index = {}

        for i, n in enumerate(nums):
            comp = target - n 
            if comp in value_index:
                return [value_index[comp], i]
            value_index[n] = i 
        
 

       
       
                


'''
{3: 0, } -> val:index 

    |
[3, 4, 5, 6]
i = 1, n = 4
comp = target - n = 3
return [map[comp], i] = [0, 1]

{4: 0, 5: 1, }
            |
nums = [4,5,6], target = 10
i = 2, n = 6 
comp = 10 - 6 = 4
return [map[comp], i] = [0, 2]


 |       -> i (0)
   |     -> j (1)
[3,4,5,6], target = 7

nums[0] + nums[1] = 3 + 4 = 7

[0, 1]

[5, 5]
 |
    |

|
     |
[4,5,6], target = 10
nums[0] + nums[2] = 10 = 10 

time: O(n2)
space: O(1)

 #i, j = 0, 1
        for i in range(len(nums)): #  no zero
            for j in range(i + 1, len(nums)): # i + 1
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
                #else:
                    #i += 1
                    #j += 1 []

 i, j = 0, len(nums) - 1 

        while i < j:
            if nums[i] + nums[j] == target:
                return [i, j]
            elif nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
        return []
'''