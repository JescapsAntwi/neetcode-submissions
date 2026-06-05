class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [float('inf')] # sentinel value (infinity)

    def push(self, val: int) -> None:
        self.stack.append(val)
        #self.min_stack = min(self.min_stack, self.stack)
        self.min_stack.append(min(val, self.min_stack[-1]))
        #.append(min(val, ))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]


# inf is used with float(inf) and float(-inf)
        
