class MinStack:

    def __init__(self):
        self.stack = []
        self.minvals = [float("inf")] # min element in stack will always be at the end of array
        self.minimum = self.minvals[-1]

    def push(self, val: int) -> None:
        if val <= self.minimum:
            self.minimum = val
            self.minvals.append(val)

        self.stack.append(val)

        # print(self.stack)

    def pop(self) -> None:
        # print("pop")
        # print(self.stack)
        top = self.stack.pop()

        if top == self.minimum:
            self.minvals.pop()
            self.minimum = self.minvals[-1]
        # print(self.stack)
        # print(self.minvals)
        # print(self.minimum)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum
