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
            if cell == "O":
                calc += ((100 * y) + x)
    return calc

with open(file_name, "r") as file:
    grid_initial, instructions_initial = file.read().split('\n\n')
    grid = [list(row) for row in grid_initial.splitlines()]
    instructions = instructions_initial.replace("\n", "")

directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

for dr in instructions:
    hit_edge = False
    robot_pos = find_robot(grid)
    next_pos = (robot_pos[0] + directions[dr][0], robot_pos[1] + directions[dr][1])
    if grid[next_pos[0]][next_pos[1]] == '#':
        continue
    if grid[next_pos[0]][next_pos[1]] == '.':
        grid[robot_pos[0]][robot_pos[1]], grid[next_pos[0]][next_pos[1]] = \
        grid[next_pos[0]][next_pos[1]], grid[robot_pos[0]][robot_pos[1]]
        continue
    if grid[next_pos[0]][next_pos[1]] == 'O':
        first_O = (next_pos[0], next_pos[1])
        while grid[next_pos[0]][next_pos[1]] == 'O':
            next_pos = (next_pos[0] + directions[dr][0], next_pos[1] + directions[dr][1])
            if grid[next_pos[0]][next_pos[1]] == '#':
                hit_edge = True
                break
        if hit_edge:
            continue
        grid[robot_pos[0]][robot_pos[1]], grid[first_O[0]][first_O[1]], grid[next_pos[0]][next_pos[1]] = \
        grid[next_pos[0]][next_pos[1]], grid[robot_pos[0]][robot_pos[1]], grid[first_O[0]][first_O[1]]
        continue

print(calc_gps(grid))
#Correct Answer: 1509074