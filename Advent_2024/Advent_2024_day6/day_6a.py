file_path = "input2024_6.txt"

map = []
location = {'pos': None, 'dir': None}
move = [(-1, 0), (0, 1), (1, 0), (0, -1)] # Up, right, down, left
directions = {'^': 0, '>': 1, 'v': 2, '<': 3} #numbers for index in move
visited = set()

with open(file_path, "r") as file:
    for y, line in enumerate(file):
        line = line.strip()
        map.append(list(line))
        for x, guard in enumerate(line):
            if guard in '^>v<':
                location['pos'] = (y, x)
                location['dir'] = directions[map[y][x]]
        
def valid_pos(pos):
    return 0 <= pos[0] < len(map) and 0 <= pos[1] < len(map[0])

while True:
    y, x = location['pos']
    direction = location['dir']
    new_pos = (y + move[direction][0], x + move[direction][1])
    visited.add(location['pos'])
    
    if not valid_pos(new_pos):
        break
    
    if map[new_pos[0]][new_pos[1]] == '#':
        direction = (direction + 1) % 4
        location['dir'] = direction
    else:
        location['pos'] = new_pos
        
print(len(visited))
#Correct Answer: 5067