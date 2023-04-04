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


    # CODECADEMY Q - COMPLETE THIS
    def remove_node(self, node_to_remove):

        current_node=self.head

        if node_to_remove == current_node:  # if the node is the head node
            self.delete_at_head()

        else:
            current_node = current_node.next

        return

    def get_node_at_index(self, index):
        current_node = self.head

        while index > 0:  # while the current node is not the head node
            current_node = current_node.next  # transverse to the next node in the ll
            index -= 1  # decrement index by 1 everytime we loop through until we find the node at our index

        return current_node  # returns the value of the node at that index

    # use two pointers which are n+1 spaces apart2
    # move both pointers to the right but 1 each time
    # when the right pointer = None , the right pointer has reached the None of the linked list (one after the tail which the tail points to)
    # and the left will be in the position one node before the node we want to delete
    # so you can do the left pointer.next == left pointer.next.next to delete the node we need to remove

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

        while current is not None:  # while you're not at the end of the list
            nxt = current.next  # temporary variable to save 'current.next'

            current.next = previous  # reversing the pointer's direction
            previous = current

            current = nxt

        return previous  # the result is stored in previous when the loop stops executing

    # correct answer below
    # https://www.youtube.com/watch?v=XIdigk956u0
    # keep in mind you can't run this here due to not actually having list 1 and list2
    # Use the original node, don't create copies of the nodes
    # As the answer we are asked to: Return the head of the merged linked list.
    def merge_two_sorted_lists(self, list1, list2):
        dummy = Node(0)  # create a dummy node to start a new linked list that we can insert node into in order
        tail = dummy  # you assign the tail pointer to the dummy node so that it's easy to add to the end of the list, you don't have to iterate through the entire ll each time

        while list1 and list2:  # while both lists are not empty - so we can compare
            if list1.data < list2.data:
                tail.next = list1  # insert the list1 node into the linked list with the dummy node
                list1 = list1.next  # now update the list1 pointer to move to the next node in the ll
            elif list2.data < list1.data:
                tail.next = list2  # insert the list2 node into the linked list with the dummy node
                list2 = list2.next  # now update the list2 pointer to move to the next node in the ll
            tail = tail.next  # move the tail pointer one to the right in the ll since we just added a node from one of the lists

        if list1:  # if list1 is the only list that's not empty - meaning list 2 is now empty and there's nothing else to compare list 1 nodes against...
            tail.next = list1  # take the remaining portion of the list and insert it to the tail of the newly formed linked list
        elif list2:  # if list2 is the only list that's not empty - meaning list 1 is now empty and there's nothing else to compare list 2 nodes against...
            tail.next = list2  # take the remaining portion of the list and insert it to the tail of the newly formed linked list

            return dummy.next  # 'the '.next' is important as we don't want to include the dummy node'

    # correct answer below
    # https://www.youtube.com/watch?v=gBTe7lFR3vc
    def LinkedListCycle(self):

        # fast and slow pointer will start at the same position
        # the next time they meet each other is how we know we have detected a cycle
        slowPointer = self.head
        fastPointer = self.head

        while fastPointer and fastPointer.next is not None:  # -> while no cycle has been detected

            slowPointer = slowPointer.next  # shifting the slow pointer one to the right
            fastPointer = fastPointer.next.next  # shifting the fast pointer two to the right

            if slowPointer == fastPointer:  # if the pointers every meet each other
                return True  # then there is a cycle

        return False  # no cycle detected

    # this is like an extension of the question above
    # Floyd's algorithm - tortoise and hare/fast and slow pointer - detecting a cycle
    # the question uses an array hence why we don't use '.next'
    # return the duplicate-no extra space allowed so no using a hash map
    # for The first intersection point, the distance between it and the beginning of the cycle is equal to the starting point distance to the beginning of the cycle (which is why we use a second slow pointer on step2)
    def FindTheDuplicateNumber(self, Array):
        # both pointers start at the beginning or the array

        slowPointer, fastPointer = 0, 0  # the pointers will always start at index 0 as it will never be a part of the cycle/duplicate

        # STEP 1 -Find where the fast and slow pointer intersect
        while True:
            slowPointer = Array[slowPointer]  # slow is set to the number it points at in the array - moves slow ahead once
            fastPointer = Array[Array[fastPointer]]  # fast is set to the number it points at in the array - nesting fast allows us to move 'fast' ahead twice
            if slowPointer == fastPointer: # if they intercept
                break

        # STEP 2 - the distance between step1's intersection and the beginning of the cycle(the duplicate number) is Equal to the start of the array and the beginning of the cycle(the duplicate number)
        # so when two first intersected slow pointer and the second new slow pointer(starting from the beginning of the array) intersect - we have found the beginning of the cycle - hence the duplicate number

        slowPointer2 = 0 # make the second slow pointer start at the beginning of the array
        while True:
            # both slow pointers move ahead by one position
            slowPointer2 = Array[slowPointer2]
            slowPointer = Array[slowPointer]
            if slowPointer == slowPointer2: # if they intercept
                return slowPointer # return the duplicate number - 'return slowPointer2' will also be valid


def remove_nth_node_from_end_of_list(self, n):
        dummy_node = Node(0)
        dummy_node.next = self.head
        left = dummy_node
        right = self.head

        # this is so the right pointer is n steps ahead of the head
        while n > 0 and right:
            right = right.next
            n -= 1

        while right:  # while right is not None
            left = left.next  # move the left and right pointer to the right once
            right = right.next

        # delete node n
        left.next = left.next.next
        return dummy_node.next  # 'the '.next' is important as we don't want to include the dummy node'

    # note we have to use .data in this question because when we make comparison we are comparing the actual Value of the nodes and not just pointer positions like in the 'linkedlistcycle' question
    # this is a nice question because since it's a sorted list, we know that if there's a duplicate value it will be next to the current value
    def remove_duplicates_from_a_sorted_linked_list(self):

        current = self.head

        while current:  # while current is not None

            # note we have to write them in this specific order as we need to ensure 'current.next' is not None FIRST otherwise if it's the otherway round but 'current.next' is None, it wouldn't have caught it out, causing an error when comparing the 'current data == None'
            while current.next and current.data == current.next.data:  # while the value next to the current value isn't None AND the current value and the value next to the current value are equal
                current.next = current.next.next  # delete node
            #  when the nodes aren't the same
            current = current.next  # move current to the next node

        return self.head  # we can return head since head never changes, no dummy node was needed

    # correct solution
    # Split list, Reverse second half of list, merge two lists
    def reorderList(self, list):

        # split list into 2
        slowPointer = self.head
        fastPointer = self.head.next

        while fastPointer and fastPointer.next is not None:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next

        list2 = slowPointer.next
        slowPointer.next = None  # here we have removed the list 2 portion from the original list to split them
        previous = None

        # reverse list2
        while list2 is not None:
            tempNode = list2.next  # we need a tempNode here as when we reverse the node we break the pointer. so tempNode keeps store of the current.next node

            list2.next = previous  # swap the direction by making your current lis2 node point to previous
            previous = list2  # update the pointer to the previous node now be your current list 2 pointer
            list2 = tempNode  # update the pointer to current list 2 node to be the next node in your list

        # merge the two half's of the list

        # note that after reversing list2, 'previous' will be set to the head of list 2

        list1 = self.head
        list2 = previous

        while list2 is not None:  # we use the list2 here only list 2 could shorter than the list1 when we split the original list into 2- so we base it off of that. For example if the list was made up of 3 nodes, the first hald of the list would be the first 3 nodes and the second half of the list would be the remaining 2 nodes
            # we need a tempNodes here because when we reverse the nodes we break the pointer. so temps keeps store of the current.next node
            tempList1 = list1.next
            tempList2 = list2.next

            list1.next = list2  # we make our current node in list 1 point to the current node of list 2
            list2.next = tempList1  # and our current list 2 to node point to the next node of list 1

            list1 = tempList1  # now the current list 1 node has been moved one to the right
            list2 = tempList2  # and the current list 2 node has been moved one to the right


    def addTwoNumbers():
        pass


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

- Reverse a linked list -
- Detect loop in a linked list -
- Return Nth node from the end in a linked list -
- Remove duplicates from a linked list -

"""
