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
