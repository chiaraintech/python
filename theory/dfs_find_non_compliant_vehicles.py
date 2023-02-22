# Write a program to find all non-compliant vehicles in a fleet management network,
# represented as a graph, 
# where compliance is represented as a binary attribute on each node.

class Node:
    def __init__(self, name, is_compliant):
        self.children = []
        self.name = name
        self.is_compliant = is_compliant

    def addChild(self, child):
        self.children.append(child)

    def is_non_compliant(self):
        if not self.is_compliant:
            return [self.name]
        else:
            non_compliant_vehicles = []
            for child in self.children:
                non_compliant_vehicles += child.is_non_compliant()
            return non_compliant_vehicles

def find_non_compliant_vehicles(root):
    return root.is_non_compliant()

# Example usage:
root = Node("Vehicle 1", True)
vehicle2 = Node("Vehicle 2", False)
vehicle3 = Node("Vehicle 3", True)
vehicle4 = Node("Vehicle 4", False)
root.addChild(vehicle2)
root.addChild(vehicle3)
vehicle3.addChild(vehicle4)

non_compliant_vehicles = find_non_compliant_vehicles(root)
print("Non-compliant vehicles:", non_compliant_vehicles)

# Output:
# Non-compliant vehicles: ['Vehicle 2', 'Vehicle 4']
