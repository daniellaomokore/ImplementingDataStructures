class MinStack:

    # lifo

    def __init__(self):
        self.MinStack = []
        self.min = None

    def push(self, val: int) -> None:
        self.MinStack.append(val)
        if self.min is None:
            self.min = val
        elif val < self.min:
            self.min = val

    def pop(self) -> None:
        if not self.MinStack:  # if the stack is empty
            return None

        popped = self.MinStack.pop()  # saves the element we popped into variable
        if popped == self.min:  # checks if the varible we popped was the minimum before
            if self.MinStack:  # if the stack is not empty
                self.min = min(
                    self.MinStack)  # set the new minimum of the stack to be the minimum of the new stack using inbuilt function
            else:  # if the stack is now empty
                self.min = None  # there's no min

    def top(self) -> int:
        if not self.MinStack:  # if the stack is empty
            return None

        return self.MinStack[-1]

    def getMin(self) -> int:
        return self.min



