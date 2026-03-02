class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if (not self.stack) or (val <= self.stack_min[-1]) :
            self.stack_min.append(val)

    def pop(self) -> None:
        if self.stack :
            popped = self.stack.pop()
            if popped == self.stack_min[-1] :
                self.stack_min.pop()
            return popped
        else : 
            print("No element")

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()