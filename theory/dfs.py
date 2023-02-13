class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        child = Node(name)
        self.children.append(child)
        return child

    def dfs(self):
        stack = [self.name]
        for child in self.children:
            stack += child.dfs()
        return stack
