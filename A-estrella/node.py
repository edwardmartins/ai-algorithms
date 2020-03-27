class Node:

    def __init__(self, parent, position):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0

    def __eq__(self, other):
        return self.position == other.position
        
