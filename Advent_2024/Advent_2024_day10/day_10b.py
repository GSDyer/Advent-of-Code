"""The only difference here to part a is changing the seen set into a list, we 
no longer care about how many unique trail ends there are, just how many ways
there are to reach them. Therefore we are not counting how many trail ends we
can reach from each starting node, but rather how many unique routes will end
at a trail end. In short, part a) unique trail ends, part b) unique routes"""
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
            seen = []
            dfs_list = [(y, x)]
            while len(dfs_list) > 0:
                node = dfs_list.pop()
                if trail_map[node[0]][node[1]] == 9:
                    seen.append(node)
                walk(node, dfs_list)
            trailhead_scores += len(seen)

print(trailhead_scores)
