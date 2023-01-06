"""
Implementing a Graph

OPERATIONS:

- add_vertices

- add edges

- get_vertices

- get_edges

"""

class Graph:

    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    # Get the keys of the dictionary
    def get_vertices(self):
        """
        2.Display graph vertices
        - we need to get keys of the graph dict,
        because they represent vertices.
        """
        return list(self.gdict.keys())

    # Find the distinct list of edges

    def get_edges(self):
        """
        3.Display graph edges
        - we have to find the pairs of the vertices which have an edge in between them.
        - create an empty list of edges
        - iterate through the edge values associated with each of the vertices
        - build a list containing the distinct group of edged found from the vertices
        """

        edge_names = []

        for vertex in self.gdict:
            for next_vertex in self.gdict[vertex]:
                if{next_vertex,vertex} not in edge_names:
                    edge_names.append({vertex, next_vertex})
        return edge_names

    # Add the vertex as a key
    def add_vertex(self, vertex):
        """
        4.Add a vertex
        - we need to add another additional key to the graph dictionary.
        """
        if vertex not in self.gdict:
            self.gdict[vertex] = []

    # Add the new edge
    def add_edge(self,edge):
        """
        5.Adding an edge
        - treat the new vertex as a tuple
        - validate if the edge is already present
        - if not then add the edge
        """
        edge =  set(edge) # set to remove duplicate edges added

        (vrtx1,vrtx2) =  tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]

    def find_shortest_path(self, graph,start, end, path = None):
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
print(g.get_vertices())
print(g.get_edges())

print(g.add_vertex("f"))
print(g.get_vertices())
print(g.get_edges())

print(g.add_edge({'a','e'}))
print(g.add_edge({'a','c'}))

print(g.get_vertices())
print(g.get_edges())

"Interview Qs"

"""
- Implement Breadth and Depth First Search

- Check if a graph is a tree or not

- Count the number of edges in a graph

- Find the shortest path between two vertices

"""
