from tkinter import *
from tkinter import messagebox
from a_star_algorithm import *

# DefaultS sizeS
CELL_SIZE = 60
GRID_SIZE = 700

# Colors
colors = {
    0: 'white',    # untried
    1: 'black',    # obstacle
    2: 'green',    # start
    3: 'red',      # finish
    4: 'orange',   # path
}

# Map
cell_map = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
]

# Put initial y final node on the map
start = (4, 0)
goal = (3, 4)
cell_map[start[0]][start[1]] = 2
cell_map[goal[0]][goal[1]] = 3

# Put result on the map
result = astar(cell_map, start, goal)

if result:
    for x, y in result[:-1]:
        cell_map[x][y] = 4

# Cell
class Cell:
    def __init__(self, grid, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.grid = grid

    def draw(self):
        top_left_x = x * CELL_SIZE
        top_left_y = y * CELL_SIZE
        bottom_rigt_x = top_left_x + CELL_SIZE
        bottom_rigt_y = top_left_y + CELL_SIZE
        self.grid.create_rectangle(top_left_y, top_left_x, bottom_rigt_y,
                                   bottom_rigt_x, fill=colors[self.value], width=2)


# Creates the main window
main_window = Tk()
main_window.title('A star algorithm')

# Creates a container for the buttons
frame = Frame(main_window)
frame.pack()
bottomframe = Frame(main_window)
bottomframe.pack(side=BOTTOM)

# Creates buttons
start_button = Button(frame, text='Start', fg='green', width=7)
start_button.pack(side=LEFT)

goal_button = Button(frame, text='Goal', fg='red', width=7)
goal_button.pack(side=LEFT)

obstacles_button = Button(frame, text='Obstacles', fg='black', width=7)
obstacles_button.pack(side=LEFT)

simulation_button = Button(frame, text='Path', fg='orange', width=7)
simulation_button.pack(side=LEFT)

# Creates the grid
grid = Canvas(main_window, width=GRID_SIZE, height=GRID_SIZE)
grid.pack()

# Prints the grid
for x in range(1, len(cell_map) + 1):
    for y in range(1, len(cell_map[0]) + 1):
        value = cell_map[x - 1][y - 1]
        c = Cell(grid, x, y, value)
        c.draw()

# Creates error message
if result is False:
    messagebox.showerror("Title", 'No hay camino alcanzable')

# Runs the main window
main_window.mainloop()
