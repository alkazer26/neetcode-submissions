class MinStack:

    def __init__(self):
        self.stack = []
        self.minvals = [] # min element in stack will always be at the end of array

    def push(self, val: int) -> None:
        if not self.minvals or val < self.minvals[-1]:        
            self.minvals.append(val)
        else: 
            self.minvals.append(self.minvals[-1])

        self.stack.append(val)

    def pop(self) -> None:
        top = self.stack.pop()
        self.minvals.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minvals[-1]
