class MinStack:

    def __init__(self):
        self.stack = []
        self.m = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.m) > 0:
            t = min(val, self.m[-1])
        else:
            t = val
        
        self.m.append(t)

    def pop(self) -> None:
        self.stack.pop()
        self.m.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.m[-1]
