"""
Implementing a Graph

OPERATIONS:

- add_vertices

- add edges

- show_vertices

- show_edges

"""

class Graph:

    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    # Get the keys of the dictionary
    def show_vertices(self):
        """
        2.Display graph vertices
        - we need to get keys of the graph dict,
        because they represent the vertices.
        """
        return list(self.graph_dict.keys())

    # Find the distinct list of edges
    def show_edges(self):
        """
        3.Display graph edges
        - we have to find the pairs of the vertices/nodes which have an edge in between them.
        - create an empty list of edge connections
        - iterate through the edge values associated with each of the vertices
        - build a list containing the distinct group of edges found from the vertices
        """
        edge_connections = []

        for node in self.graph_dict:  # accessing the keys of the graph dict --> node/vertices
            for neighbour in self.graph_dict[node]:   # accessing the values of the key value paris in the graph dict --> neighbouring edge connections
                if {node, neighbour} not in edge_connections:  # if the edge connection for the node and neighbour hasn't already been added to the list..
                    edge_connections.append({node, neighbour})  # append the edge connections to the list

        return edge_connections

    # Add the vertex as a key
    def add_vertex(self, vertex):
        """
        4.Add a vertex/node
        - we need to add another additional key to the graph dictionary.
        """
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    # Add the new edge
    def add_edge(self, node, neighbour):

        """
        4.Add an edge between two nodes
        -if one of the nodes don't already exist in the graph we create it
        -otherwise, just append the neighbour connection to the node/vertice key in the graph dict
        -prevent adding the same edge more than one by
        """

        if node not in self.graph_dict:  # if the node you want to create an edge connection from doesn't already exist...
            self.graph_dict[node] = [neighbour]   # create it and set it as a new node key and add the neighbour connection to it as a value
        else:
            self.graph_dict[node].append(neighbour)  # we append to the dict so that we can continually add edge connections to the current value when new edges are made, instead of resetting the value of the key


    # given a directed acyclic graph,
    # DFS recursion
    # find all possible paths from node 0 to node n-1 and return them in any order
    def find_all_paths_between_two_nodes(self):

        end_node = len(self.graph_dict) - 1
        result = []
        path = []
        def dfs(start, path, result):

            if start == end_node:    # if we find a complete path from the start node to the end node, we append this path to the result list
                result.append(path)

            for next_node in self.graph_dict[start]:  # for each node connected to the 'start' node by an edge
                path = path+[next_node] # add the next node to the path

                dfs(next_node, path, result) # use recursion to continue adding more nodes to the path until the path is complete and add the complete path to 'result'

        # for the dfs function to actually start working we need to call it
        dfs(0,[0])   # start is 0 since it's 0 in the question, every the path list will be initlaised with 0 since 0 will always be the start of every path


    def find_shortest_path(self, graph, start, end, path=None):
        pass

    def delete_edge(self):
        pass

    def delete_vertex(self):
        pass



# Create the dictionary with graph elements

graph_elements = {
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}
g = Graph(graph_elements)
print(g.show_vertices())
print(g.show_edges())

print(g.add_vertex("f"))
print(g.show_vertices())
print(g.show_edges())

print(g.add_edge('a','e'))
print(g.add_edge('a','c'))

print(g.show_vertices())
print(g.show_edges())

"Interview Qs"

"""
- Implement Breadth and Depth First Search

- Check if a graph is a tree or not

- Count the number of edges in a graph

- Find the shortest path between two vertices

"""
