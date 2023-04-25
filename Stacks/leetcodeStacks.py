class Solution:
    def isValidParentheses(self, s: str) -> bool:

        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for item in s:
            if item in Map.values():  # if the item is an opening bracket
                stack.append(item)  # add it to the stack
            elif stack and stack[-1] == Map[
                item]:  # else if the stack isn't empty and the last current bracket in the stack matches the closing bracket
                stack.pop()  # remove the opening bracket from the stack
            else:
                return False

        return stack == []


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



