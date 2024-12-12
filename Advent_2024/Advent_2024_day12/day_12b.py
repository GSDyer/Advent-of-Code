"""Although looking for number of edges, we instead look at number of corners
as this should be equal to number of edges for any shape, including those with
shapes missing within themselves"""

file_name = "input2024_12.txt"

grid = []

with open(file_name, "r") as file:
    for line in file:
        line = line.strip()
        grid.append(list(line))

direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)] 
# Up, up-right, right, down-right, down, down-left, left, up-left    

def valid_pos(pos):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])     

def find_area_corners(pos):
    current_area = {(pos)}
    dfs = [pos]
    corners = 0 #Corners == number of sides of shape
    while len(dfs) > 0:
        node = dfs.pop()
        for i, (dy, dx) in enumerate(direction):
            if i % 2 == 0:
                ny, nx = node[0] + dy, node[1] + dx
                if (ny, nx) not in current_area:
                    if valid_pos((nx, ny)) and grid[ny][nx] == grid[node[0]][node[1]]:
                        seen.add((ny, nx))
                        current_area.add((ny, nx))
                        dfs.append((ny, nx))
    for y, x in current_area:
        for i in range(len(direction)):
            if i % 2 == 0:
                edge_1 = (y + direction[i][0], x + direction[i][1])
                diag = (y + direction[(i+1)%8][0], x + direction[(i+1)%8][1])
                edge_2 = (y + direction[(i+2)%8][0], x + direction[(i+2)%8][1])
                if (edge_1 not in current_area and  
                    edge_2 not in current_area):
                    corners += 1
                if (edge_1 in current_area and   #Checking for inside corner,
                    edge_2 in current_area and   #such as on L shape
                    diag not in current_area):
                    corners += 1
    return len(current_area), corners

seen = set()
total_fence_price = 0
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if (y, x) in seen:
            continue
        else:
            seen.add((y,x))
            area, corners = find_area_corners((y, x))
            total_fence_price += area * corners
print(total_fence_price)
#Correct Answer: 814302