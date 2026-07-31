class MinStack:

    def __init__(self):
        self.stack = []
        self.minvals = [float("inf")] # min element in stack will always be at the end of array
        self.minimum = self.minvals[-1]

    def push(self, val: int) -> None:
        if val < self.minimum:
            self.minimum = val
        
        self.minvals.append(self.minimum)
        self.stack.append(val)

    def pop(self) -> None:
        top = self.stack.pop()
        self.minvals.pop()
        self.minimum = self.minvals[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum
