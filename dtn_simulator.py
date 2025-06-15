
class Node:
    def __init__(self, name):
        self.name = name
        self.connected_nodes = []
        self.store = []

    def connect(self, other):
        if other not in self.connected_nodes:
            self.connected_nodes.append(other)
            other.connected_nodes.append(self)

    def send_data(self, data, destination, visited=None):
        if visited is None:
            visited = set()
        visited.add(self)

        print(f"[SEND] {self.name} wants to send '{data}' to {destination.name}")

        if destination in self.connected_nodes:
            print(f"[DIRECT] {self.name} → {destination.name} | Sending directly...")
            destination.receive_data(data)
        else:
            print(f"[STORE] No direct path from {self.name} to {destination.name}. Storing for later.")
            self.store.append((data, destination, visited))

    def receive_data(self, data):
        print(f"[RECEIVE] {self.name} received data: '{data}'")

    def forward_stored_data(self):
        for packet in self.store[:]:
            data, destination, visited = packet
            forwarded = False
            for node in self.connected_nodes:
                if node in visited:
                    continue  # Avoid loops
                new_visited = visited.copy()
                new_visited.add(node)

                print(f"[FORWARD] {self.name} forwarding '{data}' to {node.name}")
                node.send_data(data, destination, visited=new_visited)
                self.store.remove(packet)
                forwarded = True
                break
            if not forwarded:
                print(f"[WAIT] {self.name} cannot forward '{data}' to {destination.name} yet.")


def simulate_ticks(nodes, tick_count=7):
    for tick in range(1, tick_count + 1):
        print(f"\n--- TICK {tick} ---")
        for node in nodes:
            node.forward_stored_data()


earth_station = Node("Earth Station")
space_satellite = Node("Space Satellite")
mars_satellite = Node("Mars Satellite")
relief_drone = Node("Relief Drone")
gaza_zone = Node("Gaza Zone (War Zone)")
earthquake_zone = Node("Earthquake Disaster Zone")
mars_rover = Node("Mars Rover")

earth_station.connect(space_satellite)
space_satellite.connect(relief_drone)
space_satellite.connect(mars_satellite)
relief_drone.connect(gaza_zone)
relief_drone.connect(earthquake_zone)
mars_satellite.connect(mars_rover)

gaza_zone.send_data("Urgent help needed in Gaza!", earth_station)
earthquake_zone.send_data("Medical supplies required!", earth_station)
mars_rover.send_data("Mars soil analysis data", earth_station)

all_nodes = [
    earth_station, space_satellite, mars_satellite,
    relief_drone, gaza_zone, earthquake_zone, mars_rover
]

simulate_ticks(all_nodes, tick_count=7)
