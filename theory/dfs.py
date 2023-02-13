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
            stack.extend(child.dfs())
        return stack

# The stack is initialized with [self.name] because the focus 
# is only on the NAMES of the nodes and not their objects. 
# The purpose of the stack in dfs is to store the names 
# of the nodes visited in the order they were visited.