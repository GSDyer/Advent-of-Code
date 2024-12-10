file_path = "input2024_8.txt"

char_pos = {}
unique_antinodes = set()
    
with open(file_path, "r") as file:
    #map_input for finding valid_antinodes, char_pos for valid antenna
    map_input = [list(line.strip()) for line in file]
    for y, row in enumerate(map_input):
        for x, char in enumerate(row):
            if char != '.':
                char_pos.setdefault(char, set()).add((y,x))

def valid_pos(pos):
    return 0 <= pos[0] < len(map_input) and 0 <= pos[1] < len(map_input[0])

def calc_antinode(position, distance, first=True):
    if first:
        return tuple(a + b for a, b in zip(position, distance))
    if not first:
        return tuple(a - b for a, b in zip(position, distance))

for char, pos in char_pos.items():
    for i, pos1 in enumerate(pos):
        for j, pos2 in enumerate(pos):
            if i != j:
                distance = (pos1[0] - pos2[0], pos1[1] - pos2[1])
                antinode1 = calc_antinode(pos1, distance, first=True)
                antinode2 = calc_antinode(pos2, distance, first=False)
                unique_antinodes.add(pos1)
                unique_antinodes.add(pos2)
                while valid_pos(antinode1):
                    unique_antinodes.add(antinode1)
                    antinode1 = calc_antinode(antinode1, distance, first=True)
                while valid_pos(antinode2):
                    unique_antinodes.add(antinode2)
                    antinode2 = calc_antinode(antinode2, distance, first=False)

print(len(unique_antinodes))
#Correct Answer: 1150
