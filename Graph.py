"""
Lucio Plancarte
"""
import os

class Graph:
    
    def __init__(self, path):
        """
        Initializes:
            1) an empty Python dictionary to represent the graph
                (as an adjacency list)
            2) the path to the text file with info about the graph
        It prints the message:
            "Initializing a Graph"
        -------------------------
        Parameters:
            path: the path for a text file containing nodes
        """
        self._graph = {}
        self._file_path = path
        print("Initializing a Graph")

    def read_graph_from_file(self):
        """
        This function  reads in a TEXT FILE containing node connnections
        and constructs an UNDIRECTED graph.
        Each line in the file is expected to contain two integers separated 
        by a comma, indicating a connection between two nodes.
        (See example of the file in the PDF)
        The keys are the nodes and the values is a Python SET of neighbors.

        Example:
        Having, file_path='example.txt'
        graph = read_graph_from_file()
        
        The representation of the graph should be an adjacency list as:
        {1: {2,3}, 2: {1,3}, 3: {1,2},...}
        """
        
        try:
            #opening the file
            if os.path.exists(self._file_path) and os.path.isfile(self._file_path):
                print("File Opened")
                with  open(self._file_path,"r") as file:
                    for line in file:
                        line = line.strip()
                        edge = line.split(",")
                        #print(f"x:{edge[0]} y:{edge[1]}")
                        if edge[0] not in self._graph:
                            self._graph[edge[0]] =[edge[1]]
                        else:
                            if edge[1] not in self._graph[edge[0]]:
                                self._graph[edge[0]].append(edge[1])

                        if edge[1] not in self._graph:
                            self._graph[edge[1]] = [edge[0]]
                        else:
                            if edge[0] not in self._graph[edge[1]]:
                                self._graph[edge[1]].append(edge[0])
                
                print("File Read")
            else:
                raise FileNotFoundError

        except FileNotFoundError:
            print("File Not Found")

        except Exception:
            print("An Error has occured.")

        finally:
            print("File Closed")
            file.close()



    def __str__(self):
        """
        Returns the content of the graph dictionary
        """
        print(self._graph)
        return ""

    def dfs(self,start,target_node):
        """
        Parameters:
        - start: The starting node for the depth-first search traversal.
        - target_node: The target node in the graph

        Returns:
        -bool: True if the target_node is found in the graph starting
                from the specified start node, False otherwise

        Description:
        This function perfomrs a depth-frist search (DFS) traversal on an
        undirected graph to determine if a specific node (target_node) is
        reachable from a given starting node (start).

        This method IMPLEMENTS the DFS algorithm, not just a loop.
        The DFS algorithm uses a STACK to explore nodes by going as deep as
        possible along each branch before backtracking.
        The function uses an built-in Python SET to track visited nodes and
        a built-in Python LIST acting as a STACK. i.e., considering the last
        element as the to of the stack.

        The alorithm continues the traversal until the stack is empty or
        the target_node is found.

        If the target_node is found, the function returns True; otherwise,
        it returns False.

        Example Usage:
        ```
        Having, graph = {"1": {"2", "3"}, "2":{"1","3"}, "3":{"1","2"}}
        Having, start_node = "1"
        Having, target_node = "2"
        result = dfs(start_node, target_node)
        In this examplee, result is True
        """

    def search(self, start_node, node_to_search):
        """
        Parameters:
        - start_node: The starting node for the DFS traversal.
        - node_to_search: The node to search for in the graph.

        Returns:
        - bool: True if the node_to_search is found in the graph
                starting from the specified start_node, False
                otherwise
        
        Description:
        This function serves as a wrapper for the DFS algorithm,
        providing a convenient interface for searching for a 
        specific node (node_to_search) in an undirected graph.

        This method is NOT a copy of the dfs() method. This method
        USES the dfs() method.

        The method first checks if the start_node is a valid node
        in the graph. If the start_node is valid, it calls the 'dfs'
        method to perform a DFS traversal starting from the specified
        node. If the start_node is not valid, an error message is 
        printed:
            "Start node ____ not valid"
        and the function returns False.
        """

    def highest_degree(self):
        """
        Returns a LIST containing the node(s) with the highest degree.
        In graph theory, the degree of a node is the number of edges
        connected to that node. In other words, the degree of a node
        is the number of neighbors it has.
        If multiple nodes have the sme highest degree, all are included.
        If the graph is empty it returns an empty list.

        Returns:
        -list: List of nodes that have the maximum degree in the graph

        Example:
        Having graph = {"1":{"2","3", "2":{"1","3","4"}, "3":{"1","2"}, "4":{"2"}}
        result = highest_degree()
        
        It returns ["2"]
        """

    def get_connections(self,node):
        """
        Returns a Python LIST containing the nodes connected to a given node
        If the node has no connections, it returns None
        """

