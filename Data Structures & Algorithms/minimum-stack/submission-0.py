class MinStack:

    def __init__(self):
        self.stack = []
        self.cmin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.cmin) == 0:
            self.cmin.append(val)
        else:
            self.cmin.append(min(self.cmin[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.cmin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.cmin[-1]
