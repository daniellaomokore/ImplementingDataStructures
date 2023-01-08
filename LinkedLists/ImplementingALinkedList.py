"""

Implementing a LinkedList

OPERATIONS:

-Insert/delete - You can insert/delete into the head, tail or at an index/position node in the linked list.

-Size - returns the size of the linked list

-Search - searches linked list for a node containing the requested data and returns that node if found

-get_node_at_index - finds the node at a certain index

"""


class Node:

    def __init__(self, data, next=None):  # nextNode is initialised as default to none when a new node is created,
        # it's assigned during the functions for different operations
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.length_count = 0

    def insert_at_head(self, data):
        if self.head is None:  # if the linked list is empty
            self.head = Node(data)
            self.length_count += 1

        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.length_count += 1

        return "{} inserted at Head.".format(data)

    def insert_at_tail(self, data):
        if self.head is None:  # if the linked list is empty
            self.head = Node(data)
            self.length_count += 1

        current_node = self.head  # We set the head node as our current node then iterate through the linked list until we reach the tail
        while True:
            if current_node.next is None:  # if the current node is the tail node,
                current_node.next = Node(data)  # set the node next to be to the node we want to insert
                self.length_count += 1
                break
            else:  # else move onto the next node in the LL
                current_node = current_node.next

        return "{} inserted at Tail.".format(data)

    def insert_at_index(self, data, index):

        if self.head == None or index == 0:  # if the list is empty or you want to insert at the first element of the list
            self.insert_at_head(data)
            return

        else:

            previous_node = self.get_node_at_index(index - 1)

            new_node = Node(data)

            new_node.next = previous_node.next  # set the new nodes next node to point to node that is
            # currently at the index you want to insert at
            previous_node.next = new_node  # set the previous node of the index to point to our new node

            self.length_count += 1

        return "{} inserted at index {}.".format(data, index)

    def delete_at_head(self):

        if self.head is None:
            print("You can't delete the head as the linked list is empty.")
        else:
            current_node = self.head  # make a copy of the LL head to variable 'current_node'

            self.head = current_node.next  # assign the head of the LL to be the node next to the head
            current_node = None  # re-assign the current node copy of the original head to None to delete it
            self.length_count -= 1
            return "Head Node deleted."

    def delete_at_tail(self):

        current_node = self.head  # We set the head node as our current node then iterate through the linked list until we reach the tail

        while current_node.next.next is not None:  # while the current node is not, node before the tail node
            current_node = current_node.next  # move to next node in the ll

        current_node.next = None  # set the node 1 before the tail node to 'None' to delete the tail node

        self.length_count -= 1

        return "Tail Node deleted."

    def delete_at_index(self, index):

        if index == 0:  # if you want to delete the first node of the ll
            self.delete_at_head()

        else:
            previous_node = self.get_node_at_index(index - 1)

            previous_node.next = previous_node.next.next  # Make the previous node to our element
            # point to the node after our element to delete it
            self.length_count -= 1

        return "Node at index {} deleted.".format(index)

    def get_node_at_index(self, index):
        current_node = self.head

        while index > 0:  # while the current node is not the head node
            current_node = current_node.next  # transverse to the next node in the ll
            index -= 1  # decrement index by 1 everytime we loop through until we find the node at our index

        return current_node  # returns the value of the node at that index

    def search(self, node):

        if self.head is None:  # if the list is empty
            return "Linked List is empty, so {} doesn't exist not here.".format(node)

        else:
            current_node = self.head
            while current_node != None:  # while the current node hasn't reached the tail

                if current_node.data == node:
                    return "{} exists in this Linked List.".format(node)

                current_node = current_node.next  # else move onto the next node in the LL

            return "{} is not in the Linked List.".format(node)

    def size(self):
        return self.length_count

    def print_LinkedList(self):

        if self.head is None:
            return "Linked List is empty, you can't print it."

        current_node = self.head  # set the head node as our current node then we will iterate through the LL to
        # print each node starting from the head

        while current_node is not None:  # while our current node is not the tail node
            print(current_node.data, "->", end=" ")  # print the data of the current node
            current_node = current_node.next  # then move to the next node in the Linked List

    def return_LinkedList(self):

        if self.head is None:
            return "Linked List is empty, you can't print it."

        theLinkedList = []
        current_node = self.head  # set the head node as our current node then we will iterate through the LL to
        # ... print each node starting from the head

        while current_node is not None:  # while our current node is not the tail node
            theLinkedList.append(
                str(current_node.data))  # parse to a string so you can later use the .join function for the arrows '-->'
            current_node = current_node.next  # then move to the next node in the Linked List
        theLinkedList.append("None")
        return " -> ".join(theLinkedList)

    "LEETCODE INTERVIEW QUESTIONS BELOW"


    # correct answer below
    # https://www.youtube.com/watch?v=G0_I-ZF0S38
    def reverse_a_linked_list(self):
        # initialise pointers
        previous = None
        current = self.head
        
        while current is not None:
            nxt = current.next  # temporary variable to save 'current.next'

            current.next = previous
            previous = current

            current = nxt

        return previous  # the result is stored in previous when the loop stops executing


    # correct answer below
    # https://www.youtube.com/watch?v=XIdigk956u0
    # keep in mind you can't run this here due to not actually having list 1 and list2
    # Use the original node, don't create copies of the nodes
    # As the answer we are asked to : Return the head of the merged linked list.
    def merge_two_sorted_lists(self, list1,list2):
        dummy = Node(0)            # create a dummy node to start a new linked list that we can insert node into in order
        tail = dummy               # you assign the tail pointer to the dummy node so that it's easy to add to the end of the list, yo don't have to iterate through the entire ll each time

        while list1 and list2: # while both lists are not empty - so we can compare
            if list1.data < list2.data:
                tail.next = list1                         # insert the list1 node into the linked list with the dummy node
                list1 = list1.next                        # now update the list1 pointer to move to the next node in the ll
            elif list2.data < list1.data:
                tail.next = list2                         # insert the list2 node into the linked list with the dummy node
                list2 = list2.next                        # now update the list2 pointer to move to the next node in the ll
            tail = tail.next                              # move the tail pointer one to the right in the ll since we just added a node from one of the lists

        if list1:                                         # if list1 is the only list that's not empty - meaning list 2 is now empty and there's nothing else to compare list 1 nodes against...
            tail.next = list1                             # take the remaining portion of the list and insert it to the tail of the newly formed linked list
        elif list2:                                       # if list2 is the only list that's not empty - meaning list 1 is now empty and there's nothing else to compare list 2 nodes against...
            tail.next = list2                             # take the remaining portion of the list and insert it to the tail of the newly formed linked list

            return dummy.next  # Return the head of the merged linked list.

    # correct answer below
    # https://www.youtube.com/watch?v=gBTe7lFR3vc
    def LinkedListCycle(self):

        # fast and slow pointer will start at the same position
        # the next time they meet each other is how we know we have detected a cycle
        slowPointer = self.head
        fastPointer = self.head

        while fastPointer and fastPointer.next is not None: # -> while no cycle has been detected

            slowPointer = slowPointer.next  # shifting the slow pointer one to the right
            fastPointer = fastPointer.next.next  # shifting the fast pointer two to the right

            if slowPointer == fastPointer:  # if the pointers every meet each other
                return True  # then there is a cycle

        return False  # no cycle detected




myLL = LinkedList()

print(myLL.insert_at_head(6))
print(myLL.insert_at_head(7))
print(myLL.insert_at_head(8))
print(myLL.insert_at_head(33))
print(myLL.insert_at_tail(5))
print(myLL.insert_at_tail(9))
print(myLL.insert_at_tail(10))

print("Size of linked list:", myLL.size())
print(myLL.search(78))
print(myLL.search(5))

print(myLL.return_LinkedList())

print(myLL.delete_at_index(1))
print(myLL.return_LinkedList())

print(myLL.insert_at_index(66, 3))
print(myLL.return_LinkedList())

print(myLL.delete_at_tail())
print(myLL.return_LinkedList())

print(myLL.delete_at_head())
print(myLL.return_LinkedList())

"Interview Qs"

"""

- Reverse a linked list
- Detect loop in a linked list
- Return Nth node from the end in a linked list
- Remove duplicates from a linked list

"""