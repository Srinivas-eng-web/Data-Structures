""" Graphs :  A graph is a non-linear data structure  consisting of nodes  (also called
 vertices) and edges connecting them

 Real world examples for graphs :
 Maps& Navigation -> cities = Nodes , Roads= Edges
 social networks -> people = nodes , friends = Edges
 Network topology --> routers = Nodes , links = Edges

 Types of graphs:
 undirected -> Edges go both ways  EX : facebook
 Directed -> One way Edge  EX: Twitter followers
 Weighted -> Each edge has cost/weight   EX: Google Maps
 unweighted --> just connections , no cost  EX: linkedin connections
 cyclic -> can loop back  EX: File system links
 Acyclic -> No cycles       EX: Task dependences

when we talk about the implementation a graph ,we are talking about how to represent  amd store
the structure of graph in memory  so we can operations like traversal ,search ..etc

1.Adjacency list (common)
2.Adjacency matix
3.Edge list(less common ,used in certain algorithms like kruslee's

1.Adjacency list : An  object is way to represent a graph where
-> Each node (vertex) is key in dictionary
-> The value is a list of all nodes it's connected to neighbours"""

#Example for Adjacency list

from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self,u,v,directed =False):
        self.graph[u].append(v)

        if not directed:
            self.graph[v].append(u)

    def print_graph(self):
        for node in self.graph:
            print(f"{node} -->  {self.graph[node]}")

g = Graph()

g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(2,3)
g.add_edge(3,4)
g.print_graph()

#output
# 0 -->  [1, 2]
# 1 -->  [0]
# 2 -->  [0, 3]
# 3 -->  [2, 4]
# 4 -->  [3]



""" What DFS .?

Depth first search -explores as far as possible along one branch before backtracking

imagine you are exploring amaze - you go deep into one path before checking the other 

when to use DFS?
Detecting the cycles 
Finding the connected components
solving mazex & puzzles
performing topology sorting (in directed graphs)
Trees and graphs traversal problems
"""
#
from collections import  defaultdict

graph = defaultdict(list)

edges = [("A","B"),("A","C"),("C","D")]

for u ,v in edges:
    graph[u].append(v)
    graph[v].append(u)

def dfs(node,visited):
    if node in visited:
        return
    print(node , end= "-->")
    visited.add(node)

    for neighbours in graph[node]:
        dfs(neighbours , visited)
visited = set()
print("DFS traversal")
dfs("A" , visited)




from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)


    def adjacent(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append((u))

        return self.graph

    def dfss(self,node,visited=None):
        if visited is None:
            visited = set()
        if node in visited:
            return
        print(node , end="-->")
        visited.add(node)

        for neighbours in self.graph[node]:
            self.dfss(neighbours,visited)

g = Graph()
g.adjacent("E","F")
g.adjacent("F","G")
g.adjacent("G","H")
g.adjacent("I","J")

print("DFS traversal ex:2")
g.dfss("E")

# output : E-->F-->G-->H-->

"""BFS = Breadth-First Search  
->Think of BFS like ripples in water:
->Start at a node
->Visit all neighbors first (level 1)
->Then their neighbors (level 2)
And so on...

Real-Life Analogy:
Imagine spreading a rumor: you tell your friends → they tell theirs → they tell theirs…"""

from collections import defaultdict ,deque
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self,u,v,directed = False):
        self.graph[u].append(v)
        if not directed:
            self.graph[v].append(u)

    def bfs(self,start):
        visited = set()
        queue = deque()

        queue.append(start)
        visited.add(start)
        while queue:
            node = queue.popleft()
            print(node ,end="-->")

            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)

g1 = Graph()
g1.add_edge("A","B")
g1.add_edge("A","C")
g1.add_edge("B","D")
g1.add_edge("C","E")
print("Breadth Traversal from A")
g1.bfs("A")

#output : A-->B-->C-->D-->E-->


""" Cycle detection patten : A cycle is path that starts and ends at the same and does not
reuse the any edge ,but visit the same again only if it start/end

Why is cycle detection is important:
Detection cycles is critical because cycles can cause errors ,insufficiences or  Vulnarabilities
in systems - especially
Networking
operating system
Databases
Depending resolution
"""

class Graph_D:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def has_cycle_until(self,node,visited,parent):
        visited.add(node)

        for neighbour in self.graph[node]:

            if neighbour not in visited:
                if self.has_cycle_until(neighbour,visited,node):
                    return True
            elif neighbour != parent:
                return True

        return False
    def has_cycle(self):
        visited = set()
        for node in self.graph:
            if node not in visited:
                if self.has_cycle_until(node , visited,None):
                    return True
        return False
C = Graph_D()
C.add_edge("A","B")
C.add_edge("A","C")
C.add_edge("C","D")
C.add_edge("D","A")
print("Cycle Detected:" if C.has_cycle() else "No Cycle Found")

# output : A-->B-->C-->D-->E-->Cycle Detected:



#Cycle detection pattern using directed method

class Graph_d:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)

    def cycle_directed_until(self,node,visited,rec_stack):
        visited.add(node)
        rec_stack.add(node)

        for neighbour in self.graph[node]:
            if neighbour not in visited:
                if self.cycle_directed_until(neighbour,visited,rec_stack):
                    return True
            elif neighbour in rec_stack:
                return True
        rec_stack.remove(node)

        return False
    def cycle(self):
        visited = set()
        rec_stack = set()
        for node in self.graph:
            if node not in visited:
                if self.cycle_directed_until(node,visited,rec_stack):
                    return True
        return False


s = Graph_d()
s.add_edge("A","B")
s.add_edge("B","C")
s.add_edge("C","A")

print("cycle is dected:" if s.cycle() else " no cycle detected ")

#cycle is dected:


