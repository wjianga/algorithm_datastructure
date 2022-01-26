import sys

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack if empty
  def is_empty (self):
    return (len (self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len (self.stack))


class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue is empty
  def is_empty (self):
    return (len (self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len (self.queue))

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def was_visited (self):
    return self.visited

  # determine the label of the vertex
  def get_label (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)

class Graph (object):
    def __init__ (self):
        self.Vertices = []
        self.adjMat = []

    # check if a vertex is already in the graph
    def has_vertex (self, label):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (label == (self.Vertices[i]).get_label()):
                return True
        return False

    # given the label get the index of a vertex
    def get_index (self, label):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1

    # add a Vertex with a given label to the graph
    def add_vertex (self, label):
        if (self.has_vertex (label)):
            return
        
        # add vertex to the list of vertices
        self.Vertices.append (Vertex (label))

        # add a new column in the adjacency matrix
        nVert = len (self.Vertices)
        for i in range (nVert - 1):
            (self.adjMat[i]).append (0)

        # add a new row for the new vertex
        new_row = []
        for i in range (nVert):
            new_row.append (0)
        self.adjMat.append (new_row)

    # add weighted directed edge to graph
    def add_directed_edge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def add_undirected_edge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # get edge weight between two vertices
    # return -1 if edge does not exist
    def get_edge_weight (self, fromVertexLabel, toVertexLabel):
        # one of both of vertices are not in the vertex list
        if ((not self.has_vertex(fromVertexLabel)) or (not self.has_vertex(toVertexLabel))):
            return -1
        elif (self.adjMat[fromVertexLabel][toVertexLabel] == 0):
            return -1
        else:
            return self.adjMat[fromVertexLabel][toVertexLabel]

    # get a list of immediate neighbors that you can go to from a vertex
    # return a list of indices or an empty list if there are none
    def get_neighbors (self, vertexLabel):
        neighbors = []
        cVert = self.get_index(vertexLabel)

        for i in range(len(self.adjMat[cVert])):
            if (self.adjMat[cVert][i] != 0):
                neighbors.append(i)
        
        return neighbors

    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex (self, v):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1

    # get a copy of the list of Vertex objects
    def get_vertices (self):
        return self.Vertices

    # do a depth first search in a graph
    def dfs (self, v):
        # create the Stack
        theStack = Stack ()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        print (self.Vertices[v])
        theStack.push (v)

        # visit all the other vertices according to depth
        while (not theStack.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex (theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print (self.Vertices[u])
                theStack.push (u)

        # the stack is empty, let us rest the flags
        nVert = len (self.Vertices)
        for i in range (nVert):
            (self.Vertices[i]).visited = False

    # do a breadth first search in a graph starting at vertex v (index)
    def bfs (self, v):
        # create the queue
        theQueue = Queue()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        theQueue.enqueue(self.Vertices[v])
        
        while (not theQueue.is_empty()):
            cVert = theQueue.dequeue()
            print(cVert)
            for i in self.get_neighbors(cVert.get_label()):
                if (self.Vertices[i].visited == False):
                    self.Vertices[i].visited = True
                    theQueue.enqueue(self.Vertices[i])
        
        # the queue is empty, let us rest the flags
        nVert = len (self.Vertices)
        for i in range (nVert):
            (self.Vertices[i]).visited = False

    # delete an edge from the adjacency matrix
    # delete a single edge if the graph is directed
    # delete two edges if the graph is undirected
    def delete_edge (self, fromVertexLabel, toVertexLabel):
        self.adjMat[self.get_index(toVertexLabel)][self.get_index(fromVertexLabel)] = 0
        self.adjMat[self.get_index(fromVertexLabel)][self.get_index(toVertexLabel)] = 0

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex (self, vertexLabel):
        vert = self.get_index(vertexLabel)

        self.Vertices.pop(vert)

        for i in self.adjMat:
            i.pop(vert)
        
        self.adjMat.pop(vert)


def main():
    # create he Graph object
    cities = Graph()

    # read the number of vertices
    line = (sys.stdin.readline()).strip()
    num_vertices = int (line)
    #print (num_vertices)

    # add the vertices to the graph
    for i in range (num_vertices):
        city = (sys.stdin.readline()).strip()
        #print (city)
        cities.add_vertex (city)

    # read the number of edges
    line = (sys.stdin.readline()).strip()
    num_edges = int (line)

    # read the edges and add them to the adjacency matrix
    for i in range (num_edges):
        line = (sys.stdin.readline()).strip()
        #print (line)
        edge = line.split()
        start = int (edge[0])
        finish = int (edge[1])
        weight = int (edge[2])

        cities.add_directed_edge (start, finish, weight)

    """
    # print the adjacency matrix
    print ("\nAdjacency Matrix")
    for i in range (num_vertices):
        for j in range (num_vertices):
            print (cities.adjMat[i][j], end = " ")
        print()
    print()
    """

    # read the starting vertex for dfs and bfs
    start_vertex = (sys.stdin.readline()).strip()

    # get the index of the starting vertex
    start_index = cities.get_index (start_vertex)

    # do the depth first search
    print ("\nDepth First Search") #+ start_vertex)
    cities.dfs (start_index)
    #print()

    # do the breadth first search
    print ("\nBreadth First Search") #+ start_vertex)
    cities.bfs (start_index)
    #print()

    fromToVer = sys.stdin.readline().strip().split()
    
    # test deletion of an edge
    print("\nDeletion of an edge")
    cities.delete_edge(fromToVer[0], fromToVer[1])
    #print()

    print("\nAdjacency Matrix")
    for i in range (num_vertices):
        for j in range (num_vertices):
            if (j == num_vertices - 1):
                print(cities.adjMat[i][j])
            else:
                print(cities.adjMat[i][j], end = " ")
        #print()
    print()

    verDel = sys.stdin.readline().strip()

    # test deletion of a vertex
    print("Deletion of a vertex")
    cities.delete_vertex(verDel)

    print("\nList of Vertices")
    for x in cities.get_vertices():
        print(x)

    print("\nAdjacency Matrix")
    for i in range (num_vertices - 1):
        for j in range (num_vertices - 1):
            if (j == num_vertices - 2):
                print(cities.adjMat[i][j])
            else:
                print(cities.adjMat[i][j], end = " ")
        #print()
    print()


    """
    line_v = sys.stdin.readline().strip()

    theGraph = Graph()

    # add vertices to the Graph
    for i in range(int(line_v)):
        theGraph.add_vertex(sys.stdin.readline().strip())

    line_e = sys.stdin.readline().strip()

    for j in range(int(line_e)):
        edge = sys.stdin.readline().strip().split()
        theGraph.add_directed_edge(int(edge[0]), int(edge[1]), int(edge[1]))

    # test depth first search
    searchV = sys.stdin.readline().strip()

    for x in theGraph.Vertices:
        print(x.label)

    print("Depth First Search")
    theGraph.dfs(theGraph.get_index(searchV))
    print("")

    # test breadth first search

    print("Breadth First Search")
    theGraph.bfs(theGraph.get_index(searchV))
    print("")

    # test deletion of an edge

    # test deletion of a vertex
    """

if __name__ == "__main__":
    main()