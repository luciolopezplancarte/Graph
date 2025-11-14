from FlightManager import FlightManager

FM = FlightManager('airports.txt')
print(f"London's destinations: {FM.show_destinations("London")}")
print(f"Can a person fly from New York to Rome? {FM.can_travel_to("New York", "Rome")")
print(f"Can a person fly from New York to Mexico? {FM.can_travel_to("New York", "Mexico")")
print(f"Can a person fly from New York to Rome? {FM.most_busy()}")
