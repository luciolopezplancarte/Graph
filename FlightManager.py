"""
Lucio Plancarte
"""
from Graph import Graph

class FlightManager(Graph):

    def __init__(self,file):
        """
        Initializes a flights network by reading the file containing the
        information about the connections.
        Parameters:
        - the file for the flights network

        Use any of the inherited methods.
        """
        super().__init__(file)
        self.read_graph_from_file()

    def show_destinations(self, city):
        """
        Returns all the flight destinations starting at a given city.
        Use any of the inherited methods.
        """
        return self.get_connections(city)

    def can_travel_to(self,source, destination):
        """
        Returns True or False if there is a path between cities
        Use any of the inheried methods
        """
        return self.search(source,destination)

    def most_busy(self):
        """
        Returns the most busy cities
        Use any of the inherited methods
        """
        return self.highest_degree()



