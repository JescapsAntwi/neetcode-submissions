class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closeToOpen = { '}': '{', ']': '[', ')': '(' }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

    


'''
stack = []
hash = { '}': '{', ']': '[', ')': '(' } close: open
      |
s = "[]"

s = "[(])"

s = "([{}])"

use stack to store opening parentheses 
go through string, if the stack isn't empty and the character we are on
is closing parentheses, check if it's opening parentheses is in the hashmap
else return false, if character isn't in hashmap, add it to the stack
check if stack is empty at the end (return True) else False

time: O(n)
stack: O(n) -> hashmap
'''