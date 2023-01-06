"""
Implementing a Stack Data structure using an Array

Top = is the pointer that points to the index of the very top value of a stack.

The value of top represents the index number for the 'top' element in the stack. If your stack has 3 elements in it
[5,33,8], the value of top will be 2, as index 2 represents the index for the top element-which has the value of '8' .

If your stack is empty, the value of top will be -1.

push - increase 'Top' (index) by 1, add your element to the top of the stack.
pop - decrease 'Top' (index) by 1, remove an element from the top of the stack.
peek - returns the actual value of element that the 'Top' pointer is pointing to  (so not it's index, the actual element).


"""


class Stack:

    # INITIALISING ALL THE RULES/FEATURES OF A STACK
    def __init__(self, capacity):   # remember to get user input for the capacity of the stack
        self.stack = []  # empty stack
        self.top = -1  # the value of 'top' is initially set to -1 as we are starting with an empty stack
        self.capacity = capacity   # stacks have a pre-defined maximum capacity
        # self.count = 0  # An alternative would be to have a count variable to track the size of the stack - that you
        # increase by 1 when pushing and decrease by 1 when popping

    # returns the size of the queue
    # size of the stack will be the pointer TOP value + 1
    def stack_size(self):
        # return self.count
        size = self.top + 1
        return size

    # the stack is full if the size of the stack == the capacity of the stack
    def stack_is_full(self):
        # return self.count == self.capacity
        return self.stack_size() == self.capacity    # this returns true if stack is full

    # the stack is empty if the size of the queue == 0
    def stack_is_empty(self):
        # return self.count == 0
        return self.stack_size() == 0    # this returns true if stack is empty



    # ADDS ITEM TO TOP OF STACK
    def push(self, value):
        # check if stack is full
        if self.stack_is_full():   # if stack is full
            return "Sorry you can't add any items to the stack, you've reached maximum capacity."

        else:  # if the queue isn't full, continue the process to push the item

            #self.count += 1   # increase count by 1
            self.top += 1  # you need to increase the value of top by 1, hence creating a space for you new value to be
            self.stack.append(value)  # then next you can add the value to the top of your stack

            return "{} has been pushed to your stack".format(value)

    # REMOVES ITEM FROM TOP OF STACK
    def pop(self):
        # check if stack is empty
        if self.stack_is_empty(): # if stack is empty
            return "Sorry, You can't remove an item as your stack is already empty."

        else:       # if your stack isn't empty, continue the process to pop an item

            # self.count -= 1   # decrease count by 1
            self.stack.pop()    # remove the top value from the stack
            self.top -= 1       # then you decrease the top value by 1
            return "An item has been popped from your stack"

    # RETURNS THE 'TOP' POINTER VALUE OF THE STACK - SO RETURNS THE ACTUAL VALUE OF THE TOP ITEM OF THE STACK (NOT IT'S INDEX]
    def peek(self):

        if self.stack_is_empty(): # if stack is empty
            return "Sorry, You can't get the top/peek value as your stack is empty."

        else:
            top_value = self.stack[self.top]
            return top_value

    # PRINTS THE ENTIRE STACK
    def print_stack(self):
        return self.stack



# Driver Code

yellasStack = Stack(3) # [none,none,none]   It will start with a capacity of 6, and size of 0

print(yellasStack.stack_is_empty())   # returns True as the stack is empty
print(yellasStack.stack_is_full())  # returns False as the stack is not full


print(yellasStack.push(6))  #[6,none,none]   capacity of 3, size of 1
print(yellasStack.push(7))  #[6,7,none]      capacity of 3, size of 2
print(yellasStack.push(7))  #[6,7,7]         capacity of 3, size of 3
print(yellasStack.peek())   # returns peek value of 7

print(yellasStack.stack_is_full())  # returns True as the stack is full
print(yellasStack.stack_is_empty())  # returns False as the stack is not empty


print(yellasStack.print_stack()) #  [6,7,7]         capacity of 3, size of 3
print(yellasStack.pop())         # [6,7,none]      capacity fof 3, size of 2
print(yellasStack.print_stack()) # [6,7,none]      capacity fof 3, size of 2
print(yellasStack.stack_size())   # returns stack size of 2



"Interview Qs"

"""
- Evaluate postfix expression using a stack

- Sort values in a stack

- Check balanced parenthesis in an expression

"""

"""
Interview add on functions would be

# the 'min stack' question

https://www.youtube.com/watch?v=qkLl7nAwDPo
"""