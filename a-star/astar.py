from math import sqrt
from heapq import heappush, heappop

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
    g_value = {}  # node, g-value
    f_value = {}  # node, f-value

    # initial node to the open list
    g_value = {start: 0}
    f_value = {start: heuristic(start, goal)}
    heappush(open_list, (f_value[start], start))

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
            temporal_g = g_value[current] + heuristic(current, neighbor)

            if 0 <= neighbor[0] < len(nmap):
                if 0 <= neighbor[1] < len(nmap[0]):
                    if nmap[neighbor[0]][neighbor[1]] == 1:
                        continue  # unwalkable terrain
                else:  # outside of map
                    continue
            else:  # outside of map
                continue

            # skip if node is already in the closed list and its value is better
            if neighbor in closed_list and temporal_g >= g_value.get(neighbor, 0):
                continue

            # update node or insert new node in the open list
            if temporal_g < g_value.get(neighbor, 0) or neighbor not in [i[1] for i in open_list]:
                came_from[neighbor] = current
                g_value[neighbor] = temporal_g
                f_value[neighbor] = temporal_g + heuristic(neighbor, goal)
                heappush(open_list, (f_value[neighbor], neighbor))
    return False
