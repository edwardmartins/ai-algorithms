from math import *
from heapq import *

def heuristic(x, y):
    return sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

def get_path(current, came_from):
    data = []
    while current in came_from:
        data.append(current)
        current = came_from[current]
    return data[::-1]

def astar(nmap, start, goal):
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0),
                 (1, 1), (1, -1), (-1, 1), (-1, -1)]

    open_list = []  # f-value, node
    closed_list = set()  # node
    came_from = {}  # node, parent
    g_values = {}  # node, g-value
    f_values = {}  # node, f-value

    # initial node to the open list
    g_values = {start: 0}
    f_values = {start: heuristic(start, goal)}
    heappush(open_list, (f_values[start], start))

    # while there is nodes in the open list keep searching
    while open_list:

        # take the node with the smallest f-value
        current = heappop(open_list)[1]

        if current == goal:
            return get_path(current, came_from)

        # add it to the closed list
        closed_list.add(current)

        # expand it
        for x, y in neighbors:
            neighbor = current[0] + x, current[1] + y
            temporal_g = g_values[current] + heuristic(current, neighbor)

            if 0 <= neighbor[0] < len(nmap):
                if 0 <= neighbor[1] < len(nmap[0]):
                    if nmap[neighbor[0]][neighbor[1]] == 'X':
                        continue  # unwalkable terrain
                else: # outside of map
                    continue
            else: # outside of map
                continue

            # skip if node is already in the closed list
            if neighbor in closed_list and temporal_g >= g_values.get(neighbor, 0):
                continue

            # update node or insert new node in the open list
            if temporal_g < g_values.get(neighbor, 0) or neighbor not in [i[1] for i in open_list]:
                came_from[neighbor] = current  
                g_values[neighbor] = temporal_g
                f_values[neighbor] = temporal_g + heuristic(neighbor, goal)
                heappush(open_list, (f_values[neighbor], neighbor))
    return False


if __name__ == "__main__":
    nmap = [
        ['X', 'X', ' ', ' ', ' '],
        [' ', 'X', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', 'X', ' ', ' ', ' '],
        [' ', 'X', ' ', ' ', ' ']]
    
    start = (4,0)
    goal = (3,4)

    result = astar(nmap, start, goal)

    print("-------------------------")
    print("A star algorithm")
    print("-------------------------")
    print("Obstacle -> X")
    print("Path     -> #")
    print("-------------------------")

    # put initial y final node on the map
    nmap[start[0]][start[1]] = "I"
    nmap[goal[0]][goal[1]] = "F"

    # put result on the map
    if(result):
        for node in result[:-1]:
            for i in range(len(nmap)):
                for j in range(len(nmap[i])):
                    if(node[0] == i and node[1] == j):
                        nmap[i][j] = '#'
    else:
        print("Impossible to reach goal")
        print("-------------------------")

    # print result
    for row in nmap:
            print(row)




