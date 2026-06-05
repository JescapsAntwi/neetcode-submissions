class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        if heights aren't in increasing order they will be popped
        stack holds index and height of bars 
        elements left in stack are bars that we could have extended all the 
        way to the end of the histogram 
        elements are pushed and popped onto the stack once 

        '''
        maxArea = 0
        stack = [] # stores pairs (index, height) of each bar 
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index 
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea