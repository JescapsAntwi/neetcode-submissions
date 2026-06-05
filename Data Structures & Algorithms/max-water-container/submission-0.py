class Solution:
    def maxArea(self, heights: List[int]) -> int:

        '''
- brute force 
- one pointer starts from first pos, second pointer starts from second
- find area using pointers
 - return max of area and result using pointers
        '''
        res = 0
        for l in range(len(heights)):
            for r in range(1 + l, len(heights)):
                area = (r - l) * min(heights[l], heights[r])
                res = max(res, area)
        return res 


        