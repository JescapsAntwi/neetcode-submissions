class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        for every n, we can have n open and n close parentheses
        we can't exceed n when we're adding open and close parentheses

        use bactracking for the order 

        we can only add a closing parentheses when the number of 
        closing parentheses is less than the number of opening parentheses

        we can only add an opening parentheses when the number of 
        opening parentheses is less than n 

        our match is valid if and only if count of open = count of close = n 
         '''
        stack = []
        result = []

        def backtrack(count_open, count_close):
            if count_open == count_close == n:
                result.append("".join(stack))
                return 
            if count_open < n:
                stack.append("(")
                backtrack(count_open + 1, count_close)
                stack.pop()

            #we can only add a close parentheses if count of close parentheses is less than open parentheses
            if count_close < count_open:
                stack.append(")")
                backtrack(count_open, count_close + 1)
                stack.pop()
        
        backtrack(0, 0) #we start the stack with an empty parentheses
        return result


