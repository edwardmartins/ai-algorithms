import math

class Node:

    def __init__(self, parent, position):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0

    def __eq__(self, other):
        return self.position == other.position

def calculateEculidianDistance(x,y):
   return math.sqrt( (x[0]-y[0])**2 + (x[1]-y[1])**2)


start = (0,0)
end = (1,1)

d = calculateEculidianDistance(start,end)

print(d)