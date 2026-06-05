class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
empty array is always a subset 
every element is a subset 


[1, 2] -> [[], [1], [2], [1, 2]]

num = 1

res = res + [subset + [num] for subset in res]

 = [] + [[] + 1]
 = [] + [] + 1 + 2

 core idea: use results to store subsets 
 - add each number to our current subsets and create new subsets 
 - then update res with the results 
        '''
        res = [[]]

        for num in nums:
            res = res + [ subset + [num] for subset in res]
        
        return res