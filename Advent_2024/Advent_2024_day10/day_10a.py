file_path = "input2024_10.txt"

trail_map = []
with open(file_path, "r") as file:
    for y, line in enumerate(file):
        trail_map.append([int(char) for char in line.strip()])
 
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)] # Up, right, down, left

def valid_pos(pos):
    return 0 <= pos[0] < len(trail_map) and 0 <= pos[1] < len(trail_map[0])      
            
def walk(pos, stack):
    for dy, dx in direction:
        ny, nx = pos[0] + dy, pos[1] + dx
        if valid_pos((ny, nx)):
            if trail_map[ny][nx] == trail_map[pos[0]][pos[1]] + 1:
                stack.append((ny, nx))

trailhead_scores = 0
for y in range(len(trail_map)):
    for x in range(len(trail_map[0])):
        if trail_map[y][x] == 0:
            seen = set()
            dfs_list = [(y, x)]
            #Depth First Search
            while len(dfs_list) > 0:
                node = dfs_list.pop()
                if trail_map[node[0]][node[1]] == 9:
                    seen.add(node)
                walk(node, dfs_list)
            trailhead_scores += len(seen)

print(trailhead_scores)
#Correct Answer: 538