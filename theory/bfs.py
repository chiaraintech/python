class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        child = Node(name)
        self.children.append(child)
        return child

    def bfs(self):
        array = []
        queue = [self]

        while queue:
            current = queue.pop(0)
            array.append(current.name)
            queue.extend(current.children)
        return array

# The queue is initialized with the current node represented as [self]
# because bfs needs to keep track of not only the NAMES of the nodes, 
# but also their actual OBJECTS in order to access their children.