import tkinter as tk 
from tkinter import messagebox
from collections import deque

# Constants
TILE_SIZE = 30
MAZE = [
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], 
  [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1], 
  [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1], 
  [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1], 
  [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1], 
  [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1], 
  [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1], 
  [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1], 
  [1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1], 
  [1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
  [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1], 
  [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1], 
  [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1], 
  [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1], 
  [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1], 
  [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1], 
  [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1], 
  [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1], 
  [1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1], 
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 
]
ROWS, COLS = len(MAZE), len(MAZE[0])

# Starting position
player_pos = [1, 1]

# AI Positions
comp_pos_1 = [1, 19]
comp_pos_2 = [18, 18]
comp_pos_3 = [8, 11]

# Exit position 
exit_pos = [20, 20]

def move_player(event):
  global player_pos
  global comp_pos_1
  global comp_pos_2
  global comp_pos_3
  new_pos = player_pos.copy()
  new_comp_pos_1 = comp_pos_1.copy()
  new_comp_pos_2 = comp_pos_2.copy()
  new_comp_pos_3 = comp_pos_3.copy()
  direction1 = ""
  direction2 = ""
  direction3 = ""

  if event.keysym == 'Up':
    new_pos[0] -= 1
  elif event.keysym == 'Down':
    new_pos[0] += 1
  elif event.keysym == 'Left':
    new_pos[1] -= 1
  elif event.keysym == 'Right':
    new_pos[1] += 1
  
  direction1 = search_for_player(comp_pos_1, new_pos)
  direction2 = search_for_player(comp_pos_2, new_pos)
  direction3 = search_for_player(comp_pos_3, new_pos)

  if direction1 == 'Up':
    new_comp_pos_1[0] -= 1
  elif direction1 == 'Down':
    new_comp_pos_1[0] += 1
  elif direction1 == 'Left':
    new_comp_pos_1[1] -= 1
  elif direction1 == 'Right':
    new_comp_pos_1[1] += 1

  if direction2 == 'Up':
    new_comp_pos_2[0] -= 1
  elif direction2 == 'Down':
    new_comp_pos_2[0] += 1
  elif direction2 == 'Left':
    new_comp_pos_2[1] -= 1
  elif direction2 == 'Right':
    new_comp_pos_2[1] += 1

  if direction3 == 'Up':
    new_comp_pos_3[0] -= 1
  elif direction3 == 'Down':
    new_comp_pos_3[0] += 1
  elif direction3 == 'Left':
    new_comp_pos_3[1] -= 1
  elif direction3 == 'Right':
    new_comp_pos_3[1] += 1

  if MAZE[new_pos[0]][new_pos[1]] == 0:
    comp_pos_1 = new_comp_pos_1
    comp_pos_2 = new_comp_pos_2
    comp_pos_3 = new_comp_pos_3
    check_caught()
    
    player_pos = new_pos
    
    draw_maze()
    check_exit()

def valid_move_check(x_pos, y_pos, visited):
  return (0 <= x_pos < len(MAZE) and 0 <= y_pos < len(MAZE[0]) and MAZE[x_pos][y_pos] == 0 and not visited[x_pos][y_pos])

def shortest_path(new_computer_position, new_position):
  visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
  directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

  queue = deque([(new_computer_position[0], new_computer_position[1], 0)])
  visited[new_computer_position[0]][new_computer_position[1]] = True

  while queue:
    x, y, distance = queue.popleft()
    
    if [x, y] == new_position:
      return distance
    
    # Explore
    for dx, dy in directions:
      new_x, new_y = x + dx, y + dy

      if valid_move_check(new_x, new_y, visited):
        visited[new_x][new_y] = True
        queue.append([new_x, new_y, distance + 1])
  
  return -1

def search_for_player(comp_position, new_position):
  path = 100
  shortest_path_name = 'None'
  if MAZE[comp_position[0] + 1][comp_position[1]] == 0: # Down
    new_comp_pos = [comp_position[0] + 1, comp_position[1]]
    path_length = shortest_path(new_comp_pos, new_position)

    if path_length < path:
      path = path_length
      shortest_path_name = 'Down'
  
  if MAZE[comp_position[0] - 1][comp_position[1]] == 0: # Up
    new_comp_pos = [comp_position[0] - 1, comp_position[1]]
    path_length = shortest_path(new_comp_pos, new_position)

    if path_length < path:
      path = path_length
      shortest_path_name = 'Up'
  
  if MAZE[comp_position[0]][comp_position[1] + 1] == 0: # Right
    new_comp_pos = [comp_position[0], comp_position[1] + 1]
    path_length = shortest_path(new_comp_pos, new_position)

    if path_length < path:
      path = path_length
      shortest_path_name = 'Right'
  
  if MAZE[comp_position[0]][comp_position[1] - 1] == 0: # Left
    new_comp_pos = [comp_position[0], comp_position[1] - 1]
    path_length = shortest_path(new_comp_pos, new_position)

    if path_length < path:
      path = path_length
      shortest_path_name = 'Left'
  
  return shortest_path_name

def check_exit():
  if player_pos == exit_pos:
    messagebox.showinfo("Congratulations!", "You've reached the exit!")
    root.quit()

def check_caught():
  if player_pos == comp_pos_1 or player_pos == comp_pos_2 or player_pos == comp_pos_3:
    messagebox.showinfo("Oh no!", "You got caught!")
    root.quit()
  
def draw_maze():
  canvas.delete('all')
  for row in range(ROWS):
    for col in range(COLS):
      color = 'black' if MAZE[row][col] == 1 else 'white'
      x1, y1 = col * TILE_SIZE, row * TILE_SIZE
      x2, y2 = x1 + TILE_SIZE, y1 + TILE_SIZE
      canvas.create_rectangle(x1, y1, x2, y2, fill=color)

  px, py = player_pos[1] * TILE_SIZE, player_pos[0] * TILE_SIZE
  canvas.create_rectangle(px, py, px + TILE_SIZE, py + TILE_SIZE, fill='lightblue')

  c1x, c1y = comp_pos_1[1] * TILE_SIZE, comp_pos_1[0] * TILE_SIZE
  canvas.create_rectangle(c1x, c1y, c1x + TILE_SIZE, c1y + TILE_SIZE, fill='red')

  c2x, c2y = comp_pos_2[1] * TILE_SIZE, comp_pos_2[0] * TILE_SIZE
  canvas.create_rectangle(c2x, c2y, c2x + TILE_SIZE, c2y + TILE_SIZE, fill='red')

  c3x, c3y = comp_pos_3[1] * TILE_SIZE, comp_pos_3[0] * TILE_SIZE
  canvas.create_rectangle(c3x, c3y, c3x + TILE_SIZE, c3y + TILE_SIZE, fill='red')

  ex, ey = exit_pos[1] * TILE_SIZE, exit_pos[0] * TILE_SIZE
  canvas.create_rectangle(ex, ey, ex + TILE_SIZE, ey + TILE_SIZE, fill='green')

root = tk.Tk()
root.title("Maze Game vs Advanced AI")

canvas = tk.Canvas(root, width=COLS * TILE_SIZE, height=ROWS * TILE_SIZE)
canvas.pack()

root.bind('<KeyPress>', move_player)

draw_maze()
root.mainloop()



