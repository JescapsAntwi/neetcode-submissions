class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
stack = [5]

1 + 2 = 3

3 * 3 = 9

9 - 4 = 5
        '''
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack[0]