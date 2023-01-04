"""

Implementing a LinkedList

OPERATIONS:

-Insert/delete - You can insert/delete into the head, end or after a given node in the linked list.

-Size - returns the size of the linked list

-Search - searches linked list for a node containing the requested data and returns that node if found

-get_node_at_index - finds the node at a certain index

"""


class Node:

    def __init__(self, data,next_node=None):  # nextNode is initialised as default to none when a new node is created, it's assigned during the functions for different operations
        self.data = data
        self.next_node = next_node


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
            new_node.next_node = self.head
            self.head = new_node
            self.length_count += 1

        return "{} has been inserted at the Head of the Linked List.".format(data)




    def insert_at_tail(self, data):
        if self.head is None:  # if the linked list is empty
            self.head = Node(data)
            self.length_count += 1

        current_node = self.head  # We set the head node as our current node then iterate through the linked list until we reach the tail
        while True:
            if current_node.next_node is None:  # if the current node is the tail node,
                current_node.next_node = Node(data)  # set the node next to be to the node we want to insert
                self.length_count += 1
                break
            else:  # else move onto the next node in the LL
                current_node = current_node.next_node

        return "{} has been inserted at the Tail of the Linked List.".format(data)

    """def insert_at_index(self, data, index):

        if index == 0:   # if the index for the head has been input
            self.insert_at_head(data)
            return

        else:
            new_node = Node(data)

            previous_node = self.get_node_at_index(index-1)
            new_node.next_node = previous_node.next_node
            previous_node.next_node = new_node

        return "The {} has been inserted at index {}".format(data, index)"""


    def delete_at_head(self):

        if self.head is None:
            print("You can't delete the head as the linked list is empty")
        else:
            current_node = self.head  # make a copy of the LL head to variable 'current_node'

            self.head = current_node.next_node  # assign the head of the LL to be the node next to the head
            current_node = None                 # re-assign the current node copy of the original head to None to delete it
            self.length_count -= 1
            return "Node at the head has been deleted"




    def delete_at_tail(self):

        current_node = self.head  # We set the head node as our current node then iterate through the linked list until we reach the tail


        while current_node.next_node.next_node != None:  # while the current node is not, node before the tail node
            current_node = current_node.next_node  # move to next node in the ll 

        current_node.next_node = None              # set the node 1 before the tail node to 'None' to delete the tail node

        self.length_count -= 1

        return "Tail has been deleted"




    def delete_at_index(self,index):

        if index == 0:   # if the index for the head has been input
            self.delete_at_head()

        previous_node = self.get_node_at_index(index-1)

        previous_node.next_node = previous_node.next_node.next_node # make the previous node to our element point to the node after our element to delete it
        self.length_count -= 1
        return "The node at index {} has been deleted".format(index)




    def get_node_at_index(self,index):
        current_node = self.head

        while index > 0:  # while the current node is not the head node
            current_node = current_node.next_node  # transverse to the next node in the ll
            index -= 1   # decrement index by 1 everytime we loop through until we find the node at our index

        return current_node  # returns the value of the node at that index




    def search(self,node):

        if self.head is None:    # if the list is empty
            return "Linked List is empty, so {} doesn't exist not here.".format(node)

        else:
            current_node = self.head
            while current_node != None:   # while the current node hasn't reached the tail

                if current_node.data == node:
                    return "{} exists in this Linked List".format(node)

                current_node = current_node.next_node   # else move onto the next node in the LL

            return "{} is not in the Linked List".format(node)




    def size(self):
        return self.length_count




    def print_LinkedList(self):

        if self.head is None:
            return "Linked List is empty, you can't print it"

        current_node = self.head                 # set the head node as our current node then we will iterate through the LL to print each node starting from the head

        while current_node is not None:          # while our current node is not the tail node
            print(current_node.data, "->", end=" ")   # print the data of the current node
            current_node = current_node.next_node     # then move to the next node in the Linked List




    def return_LinkedList(self):

        if self.head is None:
            return "Linked List is empty, you can't print it"

        theLinkedList = []
        current_node = self.head                 # set the head node as our current node then we will iterate through the LL to print each node starting from the head

        while current_node is not None:          # while our current node is not the tail node
            theLinkedList.append(str(current_node.data))  # parse to a string so you can later use the .join function for the arrows '-->'
            current_node = current_node.next_node     # then move to the next node in the Linked List
        theLinkedList.append("None")
        return " -> ".join(theLinkedList)





myLL = LinkedList()

print(myLL.insert_at_head(6))
print(myLL.insert_at_head(7))
print(myLL.insert_at_head(8))
print(myLL.insert_at_head(33))
print(myLL.insert_at_tail(5))
print(myLL.insert_at_tail(9))
print(myLL.insert_at_tail(10))
"""print(myLL.insert_after_node(86,10))"""

print(myLL.size())
print(myLL.search(7))

print(myLL.print_LinkedList())
print(myLL.return_LinkedList())

print(myLL.delete_at_head())
#print(myLL.delete_at_index(0))
print(myLL.return_LinkedList())

print(myLL.delete_at_tail())
print(myLL.return_LinkedList())
print(myLL.delete_at_tail())
print(myLL.return_LinkedList())