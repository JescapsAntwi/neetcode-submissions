class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) 

        stack = [] # holds just indices

        n = len(temperatures)
        for current_index in range(n):
            while stack and temperatures[current_index] > temperatures[stack[-1]]:
                top_index = stack.pop()
                result[top_index] = current_index - top_index 
            stack.append(current_index)
        return result


'''
[30,38,30,36,35,40,28]

[0,0,0,0,0,0,0]

curr_index = 1 

stack = [0]


[22, 21, 20]

[0, 0, 0]

[30,38,30,36,35,40,28]

[1, 4, 1, 2, 1, 0, 0]

stack to keep track of elements that have bigger elements than them 
if i find an element bigger than the element on top of my stack, i 
remove that element, update the top element of my stack and get the difference 
between the two indices of the two elements and append to my array 
do this for all elements and elements remaining on top of array will have 0 in the output list 
'''