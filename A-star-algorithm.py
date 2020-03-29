from math import *
from heapq import *


def heuristic(x, y):
    return sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)


def get_path(start, current, came_from):
    data = []
    while current in came_from:
        data.append(current)
        current = came_from[current]  # parent of
    data.append(start)
    return data[::-1]


def astar(nmap, start, goal):

    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0),
                 (1, 1), (1, -1), (-1, 1), (-1, -1)]

    open_list = []  # f value, node
    closed_list = set()  # node
    came_from = {}  # node, parent
    g_values = {}  # node, g value
    f_values = {}  # node, f value

    # initial node to the open list
    g_values = {start: 0}
    f_values = {start: heuristic(start, goal)}
    heappush(open_list, (f_values[start], start))

    # while there is nodes in the open list keep searching
    while open_list:

        # take the node with the smallest f-value
        current = heappop(open_list)[1]

        if current == goal:
            return get_path(start, current, came_from)

        # add it to the closed list
        closed_list.add(current)

        # expand it
        for x, y in neighbors:
            neighbor = current[0] + x, current[1] + y
            # neighbour "g value" is current g + distance to neighbor
            temporal_g = g_values[current] + heuristic(current, neighbor)

            if 0 <= neighbor[0] < len(nmap):
                if 0 <= neighbor[1] < len(nmap[0]):
                    if nmap[neighbor[0]][neighbor[1]] == 'X':
                        continue  # unwalkable terrain
                else:
                    # outside of map
                    continue
            else:
                # outside of map
                continue

            if neighbor in closed_list and temporal_g >= g_values.get(neighbor, 0):
                continue

            if temporal_g < g_values.get(neighbor, 0) or neighbor not in [i[1] for i in open_list]:
                came_from[neighbor] = current  # update parent
                g_values[neighbor] = temporal_g
                f_values[neighbor] = temporal_g + heuristic(neighbor, goal)
                heappush(open_list, (f_values[neighbor], neighbor))
    return False

if __name__ == "__main__":
    nmap = [
        ['X', ' ', ' ', ' ', ' '],
        [' ', 'X', ' ', ' ', ' '],
        [' ', 'X', ' ', ' ', ' '],
        [' ', 'X', ' ', ' ', ' '],
        [' ', 'X', ' ', ' ', ' ']]

    result = astar(nmap, (4, 0), ( 3, 4))

    print("-------------------------")
    print("Algoritmo A estrella")
    print("-------------------------")
    print("Obstaculo -> X")
    print("Camino    -> #")
    print("-------------------------")


    if(result):
        for node in result:
            for i in range(len(nmap)):
                for j in range(len(nmap[i])):
                    if(node[0] == i and node[1] == j):
                        nmap[i][j] = '#'

        for row in nmap:
            print(row)
    else:
        print("Impossible to reach goal")



