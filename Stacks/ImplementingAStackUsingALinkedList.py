"""
Implementing a Stack Data structure using a Linked List

Top = is the pointer that points to the index of the very top value of a stack.
'Head' refers to Top in the case of Linked Lists.

The value of top represents the 'top' node in the Stack. If your queue has 3 elements in it [5,33,8], the value of top will be '8'.

If your stack is empty, the value of top will be 'none'.

push - create a new node, assign the newNode's 'next' node to point to the current 'Top' node , re-assign newNode as
the current 'Top' node.
pop - decrease 'Top' (index) by 1, remove an element from the top of the stack.
peek - returns the actual value of element that the 'Top' pointer is pointing to  (so not it's index, the actual element).

LinkedList stacks technically can't be full so we leave that function out

"""

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None  # When you initialise a node at first it's pointer isn't pointing to anything, you decide that while making the LL

class Stack:

    # INITIALISING ALL THE RULES/FEATURES OF A STACK
    def __init__(self):   # remember to get user input for the capacity of the stack
        self.top = None  # the value of 'top' is initially set to 'None' as we are starting with an empty stack
        self.count = 0  # count variable to track the size of the stack , it's initally 0 as we start with an empty stack

    # returns the size of the stack
    def stack_size(self):
        return self.count

    # the stack is empty if the size of the stack == 0
    def stack_is_empty(self):
        # return self.count == 0
        if self.stack_size() == 0 or self.top == None:   # if stack is empty
            return True
        else:
            return False


    # ADDS ITEM TO TOP OF STACK
    def push(self, value):
        if self.stack_is_empty():   # if stack is empty
             self.top = Node(value)  # initialise a new node and set the 'Top' pointer to it
             self.count += 1   # increase the size count of the linked list by 1

        else:  # if the stack isn't empty

            newNode = Node(value)  # initialise a new node
            newNode.next = self.top # assign the node directly next to the 'newNode' to be pointing to the current 'Top' node
            self.top = newNode      # reassign the 'newNode' as current 'Top' node, since now the 'newNode' is one
            # ... node before the previous 'Top' node so the pointer needs to be updated.
            self.count += 1  # increase the size count of the linked list by 1

        return "{} has been pushed to your stack".format(value)


    # REMOVES ITEM FROM TOP OF STACK
    def pop(self):
        # check if stack is empty
        if self.stack_is_empty(): # if stack is empty
            return "Sorry, You can't remove an item as your stack is already empty."
        else:       # if your stack isn't empty, continue the process to pop an item

            poppedNode = self.top  # Assign 'poppedNode' to the current 'Top' Node of the LL
            self.top = self.top.next  # Make the 'Top' node pointer point to the node after the current 'Top' node -
            # ... so basically making the next node the 'Top' of the LL instead
            self.count -= 1         # decrease the size by one
            poppedNode.next = None  # since the node is being deleted, make it's next pointer be equal to nothing
            return "An item has been popped from your stack"

    # RETURNS THE 'TOP' ELEMENT OF THE STACK
    def peek(self):

        if self.stack_is_empty():  # if the stack is empty
            return "You can't get to top/peek value as the stack is empty"
        else:    # if not empty
            top_value = self.top.data
            return top_value

    # PRINTS THE ENTIRE STACK
    def print_stack(self):

        iternode = self.top
        if self.stack_is_empty():
            return "Stack Underflow"

        else:

            while (iternode != None):

                print(iternode.data, end="")
                iternode = iternode.next
                if (iternode != None):
                    print(" -> ", end="")

            return "\nStack Has Been Printed Above"



# Driver Code

yellasStack = Stack()

print(yellasStack.stack_is_empty())   # returns True as the stack is empty


print(yellasStack.push(6))  # 6
print(yellasStack.push(7))  # 6 -> 7
print(yellasStack.push(7))  # 6 -> 7 -> 7
print(yellasStack.peek())   # returns peek value of 7

print(yellasStack.stack_is_empty())  # returns False as the stack is not empty


print(yellasStack.print_stack()) #  6 -> 7 -> 7
print(yellasStack.pop())         # 6 -> 7
print(yellasStack.print_stack()) # 6 -> 7
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