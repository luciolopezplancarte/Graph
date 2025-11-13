from Graph import Graph

file_path = 'nodes.txt'

myGraph = Graph(file_path)

myGraph.read_graph_from_file()

print(myGraph)


