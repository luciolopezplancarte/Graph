from Graph import Graph

file_path = 'nodes.txt'

myGraph = Graph(file_path)

myGraph.read_graph_from_file()

print(myGraph)

print(myGraph.search("1","2"))
print(myGraph.search("3","6"))
print(myGraph.search("2","10"))
print(myGraph.search("15","1"))

print(myGraph.highest_degree())
print("--------------")
