"""
Implementing a Queue Data structure using a Linked List

front = is the pointer that points to the element at the very front of a queue.

The value of front represents the 'front' node in the Stack. If your queue has 3 elements in it [5,33,8], the value of front will be '5'.

If your queue is empty, the value of front will be 'none'.

push - create a new node, assign the rears 'next' node to point to the newNode , re-assign newNode as the current
'rear' node.

pop - assign variable to current front node, reassign the node directly node next to the current front
node to be the new front node, assign the node next to the as None to delete the initial front node.

peek - returns the front node of queue.

LinkedList queues technically can't be full so we leave that function out

"""

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None  # When you initialise a node at first it's pointer isn't pointing to anything, you decide that while making the LL

class Queue:

    # INITIALISING ALL THE RULES/FEATURES OF A QUEUE
    def __init__(self):   # remember to get user input for the capacity of the queue
        self.front = None  # the value of 'front' is initially set to 'None' as we are starting with an empty queue
        self.rear = None  # the value of 'rear' is initially set to 'None' as we are starting with an empty queue
        self.count = 0  # initialise the size count of the queue to 0 as it's empty, increase by 1 when pushing and decrease by 1 when popping

    # returns the size of the queue
    def queue_size(self):
        return self.count


    # the queue is empty if the size of the queue == 0
    def queue_is_empty(self):
        if self.queue_size() == 0:   # if queue is empty
            return True
        else:
            return False


    # ADDS ITEM TO REAR OF QUEUE
    def push(self, value):
        if self.queue_is_empty():   # if queue is empty
             self.front = self.rear =Node(value)  # initialise a new node and set it to be equal to both the 'front' node and 'rear' node ,
             self.count += 1   # increase the size count of the linked list by 1

        else:  # if the queue isn't empty

            newNode = Node(value)     # initialise a new node
            self.rear.next = newNode  # assign the node directly next to the current 'rear' node to point to the 'newNode'
            self.rear = newNode       # reassign the rear pointer to point to the 'newNode'
            self.count += 1           # increase the size count of the linked list by 1

        return "{} has been pushed to your queue".format(value)


    # REMOVES ITEM FROM TOP OF QUEUE
    def pop(self):
        # check if queue is empty
        if self.queue_is_empty(): # if queue is empty
            return "Sorry, You can't remove an item as your queue is already empty."

        else:       # if your queue isn't empty, continue the process to pop an item from the front of queue

            poppedNode = self.front  # Assign 'poppedNode' to the current 'front' Node of the LL
            self.front = self.front.next  # Make the 'front' node pointer point to the node after the current 'front' node -
            # ... so basically making the next node the 'front' of the LL instead
            self.count -= 1         # decrease the size by one
            poppedNode.next = None  # since the node is being deleted, make it's next pointer be equal to nothing
            return "An item has been popped from your queue"

    # RETURNS THE 'TOP' ELEMENT OF THE QUEUE
    def peek(self):

        if self.queue_is_empty():  # if the queue is empty
            return "You can't get to top/peek value as the queue is empty"
        else:    # if not empty
            top_value = self.front.data
            return top_value

    # PRINTS THE ENTIRE QUEUE
    def print_queue(self):

        iternode = self.front
        if self.queue_is_empty():
            return "Queue Underflow"

        else:

            while (iternode != None):

                print(iternode.data, end="")
                iternode = iternode.next
                if (iternode != None):
                    print(" -> ", end="")

            return "\nQueue Has Been Printed Above"



# Driver Code

yellasQueue = Queue() # [none,none,none]   It will start with a capacity of 6, and size of 0

print(yellasQueue.queue_is_empty())   # returns True as the stack is empty


print(yellasQueue.push(6))        # 6
print(yellasQueue.push(7))        # 6 -> 7
print(yellasQueue.print_queue())  # 6 -> 7
print(yellasQueue.push(7))        # 6 -> 7 -> 7
print(yellasQueue.print_queue())  # 6 -> 7 -> 7
print(yellasQueue.peek())   # returns peek value of 6

print(yellasQueue.queue_is_empty())  # returns False as the stack is not empty

print(yellasQueue.pop())      # 7 -> 7
print(yellasQueue.pop())      # 7

print(yellasQueue.print_queue())  # 7
print(yellasQueue.queue_size())   # returns queue size of 1