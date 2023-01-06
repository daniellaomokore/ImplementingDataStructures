"""

Implementing a Binary (search) Tree

OPERATIONS:

-Insert - compares the node value to the parent node and decided whether to add it as a left node or right node.
Rule:the left node must be smaller than the root node If the node is greater than the parent node it is inserted as a
right node, otherwise it's inserted left.

-Size - returns the size of the linked list

-find_value - this check if a value exists in the tree or not. When searching for a node in a tree, we transverse the
node from left to right with a parent.

- print_tree_in_order - prints the tree 'in order' which is -> left then root then right
"""


class Node:

    def __init__(self, data):
        self.data = data  # node's value
        self.left = None  # left child
        self.right = None  # right child



    # Uses recursion
    def insert(self,insert_node):

        if self.data: # if there is a parent node
            if insert_node < self.data:  # if the node you want to insert is smaller than the current node
                if self.left is None:  # if the left child of that node is empty
                    self.left = Node(insert_node)  # insert your node there
                else:   # else if the left child of the node already has a value
                    self.left.insert(insert_node)  # carry out the same operation but to that left child node -
                    # basically moving down the left side of the tree
            elif insert_node > self.data: # else if the node you want to insert is larger than the current node
                if self.right is None:  # if the right child of that node is empty
                    self.right = Node(insert_node)  # insert your node there
                else:   # else if the right child of the node already has a value
                    self.right.insert(insert_node)  # carry out the same operation but to that right child node -
                    # basically moving down the right side of the tree
        else:  # else if there isn't a parent node
            self.data = insert_node  # make the node you want to insert the parent node

        return "{} has been inserted".format(insert_node)
    # function to delete the given deepest node (d_node) in binary tree

    # function to delete element in binary tree

    # uses recursion
    def find_value(self, value):
        if value < self.data:  # if the value you want to find is smaller than the parent node
            if self.left is None:    # if the parent node has no left child
                return "{} is not Found".format(value)
            return self.left.find_value(value)  # search that node and it's child nodes to see if the value you are
            # searching for is one of them - you're basically moving down the left side of the tree
        elif value > self.data:
            if self.right is None:  # if the parent node has no right child
                return "{} is not Found".format(value)
            return self.right.find_value(value)  # search that node and it's child nodes to see if the value you are
            # searching for is one of them - you're basically moving down the right side of the tree
        else:   # if the parent node the value of node you are searching is equal
            return "{} is Found".format(value)

    # uses recursion
    def print_tree_in_order(self):
        if self.left:  # if there's a left child
            self.left.print_tree_in_order()
        print(self.data)

        if self.right:  # if there's a right child
            self.right.print_tree_in_order()


root = Node(27)
print(root.insert(14))
print(root.insert(35))
print(root.insert(31))
print(root.insert(10))
print(root.insert(9))

root.print_tree_in_order()

print(root.find_value(7))
print(root.find_value(14))

"""

We created tree with 9 10 14 27 31 35 nodes
In this tree value 7 is not there so it gives the output as 7 not found.
14 is the left child root, hence found.


"""

"Interview Qs"

# Find the minimum and maximum value in a binary search tree
# Find the minimum and maximum height of a binary search tree
# Find the height of a binary search tree
# Find kth maximum value in binary search tree
# Find nodes at "K" distance from the root
# Find ancestors of a given node in a binary tree
# Use Breadth First Search
# Use Depth First Search
# Delete a node with one child
# Delete a node with two children
# Invert a Binary Tree
