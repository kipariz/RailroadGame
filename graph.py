from settings import *

class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res


    def find_path(self, start_vertex, end_vertex, path=None):
            """ find a path from start_vertex to end_vertex 
                in graph """
            if path == None:
                path = []
            graph = self.__graph_dict
            path = path + [start_vertex]
            if start_vertex == end_vertex:
                return path
            if start_vertex not in graph:
                return None
            for vertex in graph[start_vertex]:
                if vertex not in path:
                    extended_path = self.find_path(vertex, 
                                                end_vertex, 
                                                path)
                    if extended_path: 
                        return extended_path
            return None


if __name__ == "__main__":
    g = { "A" : ["C1"],
      "B" : ["C2"],
      "C1" : ["C2", "A"],
      "C2" : ["C1", "B", "C3"],
      "C3" : ["C2"]
    }


    graph = Graph(g)
    """
    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print('The path from vertex "A" to vertex "B":')
    
    print(path)
    """
    path = graph.find_path("B", "A")

    def decode(letter):
        if ((letter=="A")or(letter=="B")):
            return railway_stations.get(letter)
        if((letter=="C2")or(letter=="C3")or(letter=="C1")):
            return [railC_place[0][int(letter[1])-1], railC_place[1][int(letter[1])-1]]
    
    def findN(start, end, i):
         
        if(end[i]>start[i]):
            n = end[i]-start[i]
        else:
            n = start[i] - end[i]
        return n 


#добавить проход в обратную сторону
    def routeFind(start, end):
        result= []
        start = decode(start)
        end = decode(end)
       

        if (start[0]==end[0]):
            if (start[1]>end[1]):
                for i in range(start[1], start[1]-findN(start, end, 1), -1):
                    result.append([start[0],i])
            else:
                for i in range(start[1], start[1]+findN(start, end, 1)):
                    result.append([start[0],i+1])
        elif (start[1]==end[1]):
            
            if (start[0]>end[0]):
                for i in range(start[0], start[0]-findN(start, end, 0), -1):
                    result.append([i, start[1]])
            else:
                for i in range(start[0], start[0]+findN(start, end, 0)):
                    result.append([i+1, start[1]])      
        else:
            result.append("error")
        
        return result
    
    print(path)
    print(decode("B"), decode("C2"), decode("C1"), decode("A"), end=" ")
    print()
    for i in range(len(path)-1):
        
        print(routeFind(path[i], path[i+1]))
        