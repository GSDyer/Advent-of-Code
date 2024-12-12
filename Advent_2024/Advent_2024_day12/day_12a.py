file_name = "input2024_12.txt"

grid = []

with open(file_name, "r") as file:
    for line in file:
        line = line.strip()
        grid.append(list(line))

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)] # Up, right, down, left    

def valid_pos(pos):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])     

def find_area_perim(pos):
    current_area = {(pos)}
    dfs = [pos]
    perimeter = 0
    while len(dfs) > 0:
        node = dfs.pop()
        for dy, dx in direction:
            ny, nx = node[0] + dy, node[1] + dx
            if (ny, nx) not in current_area:
                if not valid_pos((ny, nx)):
                    perimeter += 1
                elif grid[ny][nx] != grid[node[0]][node[1]]:
                    perimeter += 1
                else:
                    seen.add((ny, nx))
                    current_area.add((ny, nx))
                    dfs.append((ny, nx))
    return len(current_area), perimeter

seen = set()
total_fence_price = 0
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if (y, x) in seen:
            continue
        else:
            seen.add((y,x))
            area, perimeter = find_area_perim((y, x))
            total_fence_price += area * perimeter
print(total_fence_price)
#Correct Answer: 1344578