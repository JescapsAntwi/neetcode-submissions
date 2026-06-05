class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        for i in range(len(nums) - k + 1): #ensures we iterate over every possible window
            maxi = nums[i] # set max element in window to current element in window
            for j in range(i, i + k): # iterating over all elements in the window
                maxi = max(maxi, nums[j]) # update maxi if a larger element is found
            output.append(maxi) # we update the maximum of the current window 
        return output



'''
[1, 2, 1, 0, 4, 2, 6], k = 3
 |     | (2)

    |    | (2)

       |    | (4)

          |     | (4)

             |     | (6)

brute force

output = [2, 2, 4, 4, 6]
k = 3, len(nums) = 7 

            |
0, 1, 2, 3, 4 
max = 6
   4, 7 (3 times)

   max(4, 6)
'''