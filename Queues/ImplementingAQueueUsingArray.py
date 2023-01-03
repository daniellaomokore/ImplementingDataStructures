"""
Implementing a Queue Data structure using an Array

The value of front represents the index number for the 'front' element in the queue. If your queue has 3 elements in it
[5,33,8], the value of front will be 0, as index 0 represents the index for the top element-which has the value of '5' .
The front value is constant and will ALWAYS be 0 as 0 index is the first element in an array.


enqueue - increase rear pointer index by 1, increase size count by 1,  add your element to the rear of the queue.

dequeue - decrease rear pointer index by 1, decrease size count by 1, remove an element from the front of the queue.

peek - returns the actual value of element that the 'front' pointer is pointing to (so not it's index, the actual element).


"""


class Queue:

    # INITIALISING ALL THE RULES/FEATURES OF A QUEUE
    def __init__(self, capacity):  # remember to get user input for the capacity of the queue
        self.queue = []  # empty queue
        self.front = 0  # front points to the front element of the queue, so will always be at index 0 of an array
        self.rear = -1  # rear points to the index of the last element of the queue, so it's -1 here as the array is empty
        self.capacity = capacity  # queues have a pre-defined maximum capacity
        self.count = 0  # initialise the size count of the queue to 0 as it's empty, increase by 1 when you enqueue and decrease by 1 when dequeue

    # returns the size of the queue
    # size of the queue will be the pointer TOP value + 1
    def queue_size(self):
        return self.count

    # the queue is full if the size of the queue == the capacity of the queue
    def queue_is_full(self):
        return self.queue_size() == self.capacity  # this returns true if queue is full

    # the queue is empty if the size of the queue == 0
    def queue_is_empty(self):
        return self.queue_size() == 0  # this returns true if queue is empty

    # ADDS ITEM TO REAR OF QUEUE
    def enqueue(self, value):
        # check if queue is full
        if self.queue_is_full():  # if queue is full
            return "Sorry you can't add any items to the queue, you've reached maximum capacity."

        else:  # if the queue isn't full, continue the process to push the item

            self.count += 1  # increase count by 1
            self.queue.append(value)  # then next you can add the value to the rear of your queue
            self.rear += 1  # increase rear index by 1

            return "{} has been enqueued to your queue".format(value)

    # REMOVES ITEM FROM FRONT OF QUEUE
    def dequeue(self):
        # check if queue is empty
        if self.queue_is_empty():  # if queue is empty
            return "Sorry, You can't remove an item as your queue is already empty."

        else:  # if your queue isn't empty, continue the process to pop an item

            self.queue.pop(self.front)  # remove the front value from the queue
            self.count -= 1  # decrease count by 1
            self.rear -= 1  # decrease rear index by 1

            return "An item has been dequeued from your queue"

    # RETURNS THE 'FRONT' POINTER VALUE OF THE QUEUE - SO RETURNS THE ACTUAL VALUE OF THE FRONT ITEM OF THE QUEUE (NOT IT'S INDEX]
    def peek(self):

        if self.queue_is_empty():  # if queue is empty
            return "Sorry, You can't get the top/peek value as your queue is empty."

        else:
            top_value = self.queue[self.front]
            return top_value

    # PRINTS THE ENTIRE STACK
    def print_queue(self):
        return self.queue


#  Driver Code

yellasQueue = Queue(3)  # [none,none,none]   It will start with a capacity of 6, and size of 0

print(yellasQueue.queue_is_empty())  # returns True as the queue is empty
print(yellasQueue.queue_is_full())  # returns False as the queue is not full

print(yellasQueue.enqueue(6))  # [6,none,none]   capacity of 3, size of 1
print(yellasQueue.enqueue(7))  # [6,7,none]      capacity of 3, size of 2
print(yellasQueue.enqueue(7))  # [6,7,7]         capacity of 3, size of 3
print(yellasQueue.peek())  # returns peek value of 6

print(yellasQueue.queue_is_full())  # returns True as the queue is full
print(yellasQueue.queue_is_empty())  # returns False as the queue is not empty

print(yellasQueue.print_queue())  # [6,7,7]           capacity of 3, size of 3
print(yellasQueue.enqueue(6))
print(yellasQueue.dequeue())  # [7,7,none]      capacity fof 3, size of 2

print(yellasQueue.print_queue())  # [7,7,none]      capacity fof 3, size of 2
print(yellasQueue.queue_size())  # returns queue size of 2
