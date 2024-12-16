file_name = "input2024_15.txt"

def find_robot(grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '@':
                return(y, x)
        
def calc_gps(grid):
    calc = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "[":
                calc += ((100 * y) + x)
    return calc

def box_move_list(box_left, box_right, dr):
    if dr == '<': #Quick fix for boxes breaking up when moved from the right
        move_list = [box_right, box_left]
    else:
        move_list = [box_left, box_right]
    i = 0
    no_move = False
    while i < len(move_list):
        y, x = move_list[i]
        ny, nx = y + directions[dr][0], x + directions[dr][1]
        if double_grid[ny][nx] in "[]":
            if (ny, nx) not in move_list:
                move_list.append((ny, nx))
            if double_grid[ny][nx] == '[':
                if (ny, nx + 1) not in move_list:
                    move_list.append((ny, nx + 1))
            if double_grid[ny][nx] == ']':
                if (ny, nx - 1) not in move_list:
                    move_list.append((ny, nx - 1))
        elif double_grid[ny][nx] == '#':
            no_move = True
            break
        i += 1
    if no_move:
        return []
    else:
        return move_list

with open(file_name, "r") as file:
    grid_initial, instructions_initial = file.read().split('\n\n')
    grid = [list(row) for row in grid_initial.splitlines()]
    instructions = instructions_initial.replace("\n", "")

directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
double_grid = []

for row in grid:
    double_row = []
    for char in row:
        if char == '#':
            double_row.extend(['#', '#'])
        elif char == '.':
            double_row.extend(['.', '.'])
        elif char == 'O':
            double_row.extend(['[', ']'])
        else:
            double_row.extend(['@', '.'])
    double_grid.append(double_row)

for dr in instructions:
    robot_pos = find_robot(double_grid)
    next_pos = (robot_pos[0] + directions[dr][0], robot_pos[1] + directions[dr][1])
    if double_grid[next_pos[0]][next_pos[1]] == '#':
        continue
    if double_grid[next_pos[0]][next_pos[1]] == '.':
        double_grid[robot_pos[0]][robot_pos[1]], double_grid[next_pos[0]][next_pos[1]] = \
        double_grid[next_pos[0]][next_pos[1]], double_grid[robot_pos[0]][robot_pos[1]]
        continue
    if double_grid[next_pos[0]][next_pos[1]] == ']':
        box_left = ((next_pos[0], next_pos[1] - 1))
        box_right = ((next_pos[0], next_pos[1]))
    elif double_grid[next_pos[0]][next_pos[1]] == '[':
        box_left = ((next_pos[0], next_pos[1]))
        box_right = ((next_pos[0], next_pos[1] + 1))
    move_list = box_move_list(box_left, box_right, dr)
    move_list.insert(0, robot_pos)
    if len(move_list) <= 1:
        continue
    for i in range(len(move_list)):
        box_to_move = move_list.pop()
        empty_space = (box_to_move[0] + directions[dr][0], box_to_move[1] + directions[dr][1])
        double_grid[box_to_move[0]][box_to_move[1]], double_grid[empty_space[0]][empty_space[1]] = \
        double_grid[empty_space[0]][empty_space[1]], double_grid[box_to_move[0]][box_to_move[1]]
    
print(calc_gps(double_grid))
#Correct Answer: 1521453