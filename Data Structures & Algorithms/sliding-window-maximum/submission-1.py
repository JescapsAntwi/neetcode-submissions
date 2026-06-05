class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque() # stores indices of elements that could be the maximum
        l= r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            #ensure the deque only contains indices of elements within the current window
            if l > q[0]:
                q.popleft()
            
            #check if the current window size has reached k 
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1 # slide window forward 
            r += 1 # expand the window by moving the right pointer 
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